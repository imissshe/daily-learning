# Python reversed()：反向迭代，不改原序列

> 补记 · 2026-11-15（每日贡献补齐）

reversed() 返回反向迭代器，不修改原序列；想拿列表要再包一层 list()。

```python
reversed([1, 2, 3])  # 迭代器，依次产出 3, 2, 1
list(reversed("abc"))  # ['c', 'b', 'a']
```
