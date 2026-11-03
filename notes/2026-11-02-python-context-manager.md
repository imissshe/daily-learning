# Python 上下文管理器：`with` 语句与 `contextlib`

> Day 6 · 2026-11-02 · 📝 笔记

## 为什么要用 `with`
打开文件、加锁、数据库连接这类资源，用完必须释放。`with` 保证**无论代码块是否抛异常**，清理逻辑都会执行，比手写 `try/finally` 更简洁。

```python
with open("demo.txt", "w") as f:
    f.write("hello")
# 离开 with 块时 f 已自动关闭
print(f.closed)  # True
```

## 原理：`__enter__` / `__exit__`
`with obj as x:` 会调用 `obj.__enter__()`，其返回值赋给 `x`；离开时调用 `obj.__exit__(exc_type, exc, tb)`。若 `__exit__` 返回 `True`，异常会被吞掉。

```python
import time

class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self
    def __exit__(self, exc_type, exc, tb):
        self.elapsed = time.perf_counter() - self.start
        return False  # 不吞异常

with Timer() as t:
    sum(range(1_000_000))
print(f"耗时 {t.elapsed:.4f}s")
```

## 更简单：`contextlib.contextmanager`
用生成器写，`yield` 之前是 enter，之后（放在 `finally` 里）是 exit。

```python
from contextlib import contextmanager
import os

@contextmanager
def cd(path):
    old = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(old)   # 即使出错也会切回原目录

with cd("/tmp"):
    print(os.getcwd())  # /tmp
```

## 常用现成工具
```python
from contextlib import suppress, ExitStack

# 忽略指定异常
with suppress(FileNotFoundError):
    os.remove("not-exist.txt")

# 动态管理多个资源
with ExitStack() as stack:
    files = [stack.enter_context(open(f"f{i}.txt", "w")) for i in range(3)]
# 三个文件全部已关闭
```

## 要点
- 只要有“获取 → 释放”配对，就考虑写成上下文管理器。
- `@contextmanager` 里一定把清理代码放进 `finally`。
- `__exit__` 返回 `True` 会吞异常，除非确实需要，否则返回 `False`/`None`。
- Python 3.10+ 支持括号写多个：`with (open(a) as f, open(b) as g):`。
