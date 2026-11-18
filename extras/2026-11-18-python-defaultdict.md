# Python defaultdict：免判 key 是否存在

> 补记 · 2026-11-18（每日贡献补齐）

collections.defaultdict 访问不存在的 key 时自动用工厂函数建默认值，写分组、计数代码时不用先判断 key 在不在。

```python
from collections import defaultdict
d = defaultdict(list)
d["a"].append(1)  # {'a': [1]}
```
