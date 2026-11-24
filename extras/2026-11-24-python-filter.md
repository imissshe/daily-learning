# Python filter()：惰性筛选

> 补记 · 2026-11-24（每日贡献补齐）

filter(func, iterable) 只保留 func 返回真值的元素，是惰性的；func 传 None 时过滤掉所有假值。

```python
list(filter(None, [0, 1, "", "a"]))  # [1, 'a']
```
