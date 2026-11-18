# Python asyncio 实战：async/await、gather、Semaphore 限流、超时与取消

> Day 21 · 2026-11-17 · 📝 笔记 Note
> 适用：Python 3.11+（`asyncio.TaskGroup`、`asyncio.timeout` 需要 3.11）

## 1. 什么时候用 asyncio

- **适合 I/O 密集**：大量网络请求、数据库查询、等待外部服务——等待期间让出控制权，单线程就能并发成百上千个任务。
- **不适合 CPU 密集**：纯计算会阻塞事件循环，应使用 `multiprocessing` / `concurrent.futures.ProcessPoolExecutor`。
- 核心概念：
  - **协程 coroutine**：`async def` 定义的函数，调用后得到协程对象，**不会立刻执行**。
  - **事件循环 event loop**：调度协程；`asyncio.run()` 创建并运行它。
  - **await**：挂起当前协程，直到被等待对象完成，期间循环去跑别的任务。
  - **Task**：被调度到循环中"后台运行"的协程（`asyncio.create_task`）。

## 2. 顺序 vs 并发

```python
import asyncio, time

async def fetch(name: str, delay: float) -> str:
    await asyncio.sleep(delay)          # 模拟网络 I/O；千万别用 time.sleep
    return f"{name} done"

async def sequential():
    return [await fetch("a", 0.2), await fetch("b", 0.2), await fetch("c", 0.2)]

async def concurrent():
    return await asyncio.gather(fetch("a", 0.2), fetch("b", 0.2), fetch("c", 0.2))

for fn in (sequential, concurrent):
    t = time.perf_counter()
    res = asyncio.run(fn())
    print(fn.__name__, res, f"{time.perf_counter() - t:.2f}s")
# sequential ['a done', 'b done', 'c done'] 0.60s
# concurrent ['a done', 'b done', 'c done'] 0.20s
```

要点：`gather` 返回结果的**顺序与传入顺序一致**，而不是完成顺序。

## 3. create_task：先启动、后等待

```python
async def main():
    t1 = asyncio.create_task(fetch("x", 0.3))   # 立刻被调度
    t2 = asyncio.create_task(fetch("y", 0.1))
    # ……这里可以做别的事
    print(await t2, await t1)
asyncio.run(main())
```

⚠️ 一定要保存 Task 的引用（变量/集合），否则可能被垃圾回收导致任务"消失"。

## 4. TaskGroup（3.11+）：结构化并发，推荐

```python
async def boom():
    await asyncio.sleep(0.05)
    raise ValueError("bad")

async def main():
    try:
        async with asyncio.TaskGroup() as tg:
            tg.create_task(fetch("slow", 1))
            tg.create_task(boom())
    except* ValueError as eg:                      # 异常以 ExceptionGroup 抛出
        print("caught:", [str(e) for e in eg.exceptions])
asyncio.run(main())
# caught: ['bad']   —— 且 "slow" 任务被自动取消，不会泄漏
```

对比 `gather`：默认一个任务出错时其余任务**继续跑**（没人等它们）；`gather(..., return_exceptions=True)` 则把异常当作结果返回。需要"一个失败全部取消"时用 TaskGroup。

## 5. Semaphore 限流：控制并发数

请求 100 个 URL，但同时最多 5 个，避免打爆对方或被限流：

```python
async def limited_fetch(sem: asyncio.Semaphore, i: int, stats: dict) -> int:
    async with sem:
        stats["now"] += 1
        stats["peak"] = max(stats["peak"], stats["now"])
        await asyncio.sleep(0.01)
        stats["now"] -= 1
        return i * i

async def main():
    sem = asyncio.Semaphore(5)
    stats = {"now": 0, "peak": 0}
    res = await asyncio.gather(*(limited_fetch(sem, i, stats) for i in range(100)))
    print(sum(res), "peak concurrency =", stats["peak"])   # 328350 peak concurrency = 5
asyncio.run(main())
```

## 6. 超时与取消

```python
async def main():
    # 方式一：wait_for
    try:
        await asyncio.wait_for(fetch("slow", 1), timeout=0.1)
    except TimeoutError:            # 3.11 起 asyncio.TimeoutError 就是内置 TimeoutError
        print("wait_for timeout")

    # 方式二（3.11+）：asyncio.timeout 上下文，可包住多步操作
    try:
        async with asyncio.timeout(0.1):
            await fetch("step1", 0.05)
            await fetch("step2", 0.5)
    except TimeoutError:
        print("block timeout")

    # 手动取消：被取消的协程内部会收到 CancelledError，可在 finally 里清理
    async def worker():
        try:
            await asyncio.sleep(10)
        finally:
            print("cleanup")
    t = asyncio.create_task(worker())
    await asyncio.sleep(0.01)
    t.cancel()
    try:
        await t
    except asyncio.CancelledError:
        print("cancelled:", t.cancelled())
asyncio.run(main())
```

⚠️ 捕获 `CancelledError` 后通常要**重新抛出**，吞掉它会让取消失效。

## 7. 按完成顺序处理：as_completed

```python
async def main():
    coros = [fetch("a", 0.3), fetch("b", 0.1), fetch("c", 0.2)]
    for fut in asyncio.as_completed(coros):
        print(await fut)        # b done → c done → a done
asyncio.run(main())
```

## 8. 在协程里调用阻塞代码：to_thread

```python
import time
def blocking_io(x):              # 比如老旧的同步 SDK / requests
    time.sleep(0.2)
    return x * 2

async def main():
    res = await asyncio.gather(*(asyncio.to_thread(blocking_io, i) for i in range(3)))
    print(res)                   # [0, 2, 4]，总耗时约 0.2s
asyncio.run(main())
```

## 9. 常见坑速查

| 坑 | 现象 | 正确做法 |
|---|---|---|
| 调用协程忘了 `await` | `RuntimeWarning: coroutine ... was never awaited` | `await f()` 或 `create_task(f())` |
| 协程里用 `time.sleep` / `requests` | 整个循环卡住，并发失效 | `asyncio.sleep`、`aiohttp`/`httpx.AsyncClient`，或 `to_thread` |
| 在已运行的循环里再 `asyncio.run` | `RuntimeError: asyncio.run() cannot be called from a running event loop`（如 Jupyter） | Jupyter 中直接 `await main()` |
| `create_task` 不保存引用 | 任务偶发"消失" | 存到变量或 `set`，完成后 `discard` |
| 吞掉 `CancelledError` | 无法取消、关闭卡住 | 清理后 `raise` |
| 无限制并发 | 被限流 / 文件句柄耗尽 | `Semaphore` 或连接池上限 |

## 10. 一句话总结

`async def` 定义协程，`await` 让出控制权；并发用 `gather` / `TaskGroup`，限流用 `Semaphore`，超时用 `asyncio.timeout`，阻塞代码丢给 `to_thread`。
