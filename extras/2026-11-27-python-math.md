# Python math：gcd / isqrt / isclose

> 补记 · 2026-11-27（每日贡献补齐）

math.gcd() 最大公约数，math.isqrt() 整数平方根；浮点数不要用 == 比较，用 math.isclose()。

```python
import math
math.gcd(12, 18)              # 6
math.isclose(0.1 + 0.2, 0.3)  # True
```
