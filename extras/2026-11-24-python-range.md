# Python range()：半开区间，不占内存

> 补记 · 2026-11-24（每日贡献补齐）

range() 生成半开区间 [start, stop)，不实际建出列表，再大也不占内存；step 可以为负实现倒数。

```python
list(range(3))          # [0, 1, 2]
list(range(5, 0, -2))   # [5, 3, 1]
```
