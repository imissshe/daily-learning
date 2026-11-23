# 正则 |：二选一

> 补记 · 2026-11-23（每日贡献补齐）

| 表示左右二选一；注意它的优先级最低，想限制范围要用括号括起来，如 (ab|cd)。

```python
import re
re.fullmatch(r"cat|dog", "dog")  # 匹配
```
