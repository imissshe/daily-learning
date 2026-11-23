# Python sorted()：key 与 reverse

> 补记 · 2026-11-23（每日贡献补齐）

sorted() 返回新列表，不改原序列；key 传函数决定排序依据，reverse=True 倒序。原地排序用 list.sort()。

```python
sorted(["bb", "a", "ccc"], key=len)  # ['a', 'bb', 'ccc']
```
