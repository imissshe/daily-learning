# 正则 flags：re.I 与 re.M

> 补记 · 2026-11-23（每日贡献补齐）

re.I 忽略大小写，re.M 让 ^ 和 $ 匹配每一行的开头结尾（而不只是整个字符串的开头结尾）。

```python
import re
re.search(r"^b", "a\nb", re.M)  # 匹配
re.fullmatch(r"abc", "ABC", re.I)  # 匹配
```
