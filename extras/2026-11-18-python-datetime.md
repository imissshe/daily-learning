# Python datetime：现在时间与日期

> 补记 · 2026-11-18（每日贡献补齐）

datetime.now() 取当前时间，date.today() 取今天日期；涉及时区要带 tzinfo，否则是“天真时间”，跨时区会算错。

```python
from datetime import date, datetime
date.today()            # 如 date(2026, 11, 15)
datetime.now().strftime("%Y-%m-%d %H:%M")
```
