# Python pathlib：用对象代替字符串拼路径

> 补记 · 2026-11-26（每日贡献补齐）

Path 对象用 / 拼接路径，比字符串拼接直观；exists()、read_text()、glob() 都可以直接调。

```python
from pathlib import Path
p = Path("notes") / "2026-11-15.md"
p.exists()
```
