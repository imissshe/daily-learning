# Python itertools.chain：连接多个可迭代对象

> 补记 · 2026-11-18（每日贡献补齐）

chain() 把多个可迭代对象首尾相接成一个惰性序列，不用先拼成大列表。

```python
from itertools import chain
list(chain([1, 2], [3, 4]))  # [1, 2, 3, 4]
```
