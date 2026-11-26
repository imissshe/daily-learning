# Python Counter：计数与 most_common

> 补记 · 2026-11-26（每日贡献补齐）

collections.Counter 统计元素出现次数；most_common(n) 取出频率最高的前 n 个。

```python
from collections import Counter
Counter("abracadabra").most_common(2)  # [('a', 5), ('b', 2)]
```
