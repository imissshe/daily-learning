# Python re：search / match / fullmatch

> 补记 · 2026-11-18（每日贡献补齐）

re.search() 在全文里找，re.match() 只从开头找，re.fullmatch() 要求整个字符串都匹配；校验格式用 fullmatch 最稳。

```python
import re
re.fullmatch(r"\d+", "123")   # 匹配
re.fullmatch(r"\d+", "12a")   # 不匹配
```
