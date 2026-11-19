# Python os.environ：读环境变量

> 补记 · 2026-11-19（每日贡献补齐）

os.environ 读环境变量；用 getenv(key, default) 可以带默认值，避免 key 不存在时抛 KeyError。

```python
import os
os.getenv("HOME", "/tmp")
```
