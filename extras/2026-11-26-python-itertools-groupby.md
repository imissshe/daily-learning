# Python itertools.groupby：分组前要先排序

> 补记 · 2026-11-26（每日贡献补齐）

groupby() 按 key 把连续相同的元素分到一组；输入必须先按同一 key 排好序，否则相同 key 会被拆成多组。

```python
from itertools import groupby
data = sorted([("a", 1), ("b", 2), ("a", 3)], key=lambda x: x[0])
{k: list(v) for k, v in groupby(data, key=lambda x: x[0])}
```
