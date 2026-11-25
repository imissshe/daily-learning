# Python open()：with 与编码

> 补记 · 2026-11-25（每日贡献补齐）

open() 配合 with 语句用完自动关闭文件；读写文本时显式指定 encoding="utf-8"，避免跨平台乱码。

```python
with open("a.txt", encoding="utf-8") as f:
    text = f.read()
```
