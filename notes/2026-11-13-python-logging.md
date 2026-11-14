# Python logging 实战：别再用 print 调试了

> Day 17 · 2026-11-13 · 📝 笔记

`print` 适合临时看一眼，但项目里需要**分级别、带时间和位置、可同时输出到终端和文件、可按模块开关**的日志。标准库 `logging` 全都能做。

## 1. 核心概念（四件套）

| 组件 | 作用 |
|---|---|
| **Logger** | 你调用的对象：`logger.info(...)`。按名字分层，`"app.db"` 是 `"app"` 的子 logger |
| **Handler** | 决定日志去哪：终端 `StreamHandler`、文件 `FileHandler`、轮转文件 `RotatingFileHandler` |
| **Formatter** | 决定一行日志长什么样 |
| **Level** | `DEBUG < INFO < WARNING < ERROR < CRITICAL`，低于阈值的直接丢弃 |

一条日志要同时通过 **logger 的级别** 和 **handler 的级别** 才会输出。子 logger 的记录默认会**向上传播（propagate）**给父 logger 的 handler。

## 2. 最小可用：脚本里一行配置

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-8s %(name)s:%(lineno)d - %(message)s",
)
log = logging.getLogger(__name__)

log.debug("不会输出：低于 INFO")
log.info("服务启动，端口=%d", 8080)      # 用 %s 占位，而不是 f-string
log.warning("磁盘剩余 %.1f%%", 9.5)
```

要点：
- **每个模块用 `logging.getLogger(__name__)`**，日志里就能看出来源模块。
- **传参而不是 f-string**：`log.debug("x=%s", big_obj)` 在 DEBUG 被关闭时不会去格式化 `big_obj`，更省。
- `basicConfig` 只在 root logger 还没有 handler 时生效，**只在程序入口调用一次**；库代码里不要调用它。

## 3. 记录异常：用 `log.exception`

```python
try:
    1 / 0
except ZeroDivisionError:
    log.exception("计算失败")   # = log.error(..., exc_info=True)，自动附上完整 traceback
```

## 4. 终端 + 文件，不同级别

```python
import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger("app")
logger.setLevel(logging.DEBUG)          # logger 放行所有，交给 handler 过滤

console = logging.StreamHandler()
console.setLevel(logging.INFO)          # 终端只看 INFO 及以上
console.setFormatter(logging.Formatter("%(levelname)s %(message)s"))

file = RotatingFileHandler("app.log", maxBytes=1_000_000, backupCount=3, encoding="utf-8")
file.setLevel(logging.DEBUG)            # 文件里留全部细节，超过 1MB 轮转，保留 3 份
file.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(name)s - %(message)s"))

logger.addHandler(console)
logger.addHandler(file)

logger.getChild("db").debug("SQL: SELECT 1")   # 只进文件
logger.info("用户登录")                         # 终端和文件都有
```

## 5. 用 dictConfig 集中配置（推荐中大型项目）

```python
import logging.config

logging.config.dictConfig({
    "version": 1,
    "disable_existing_loggers": False,   # 别把第三方库已创建的 logger 静音
    "formatters": {"std": {"format": "%(asctime)s %(levelname)s %(name)s - %(message)s"}},
    "handlers": {"console": {"class": "logging.StreamHandler", "formatter": "std"}},
    "root": {"level": "INFO", "handlers": ["console"]},
    "loggers": {"urllib3": {"level": "WARNING"}},   # 压低吵闹的第三方库
})
```

## 6. 库作者的规矩

库里只写：

```python
import logging
logging.getLogger(__name__).addHandler(logging.NullHandler())
```

不要在库里 `basicConfig` 或添加输出 handler——怎么输出由使用者的应用决定。

## 7. 常见坑

- **日志重复打印两次**：子 logger 和 root 都挂了 handler，记录传播后被输出两遍。只在一处挂 handler，或设置 `logger.propagate = False`。
- **`basicConfig` 没效果**：之前已有代码（或某个库）给 root 加过 handler。Python 3.8+ 可用 `basicConfig(..., force=True)` 强制重置。
- **级别设了 DEBUG 还是看不到**：logger 和 handler 两层都要放行。
- **在 handler 里用 `%` 格式化写错参数个数**：logging 不会抛异常中断程序，而是打印 `--- Logging error ---`，注意看 stderr。

## 8. 一键验证

```bash
python3 - <<'EOF'
import io, logging
buf = io.StringIO()
lg = logging.getLogger("demo"); lg.setLevel(logging.DEBUG); lg.propagate = False
h = logging.StreamHandler(buf); h.setLevel(logging.INFO)
h.setFormatter(logging.Formatter("%(levelname)s:%(name)s:%(message)s"))
lg.addHandler(h)
lg.debug("hidden"); lg.getChild("db").info("q=%d", 3)
print(buf.getvalue(), end="")   # -> INFO:demo.db:q=3
EOF
```

## 参考

- 官方教程：<https://docs.python.org/3/howto/logging.html>
- Logging Cookbook：<https://docs.python.org/3/howto/logging-cookbook.html>
