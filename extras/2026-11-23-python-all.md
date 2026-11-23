# Python all()：全部为真才为真

> 补记 · 2026-11-23（每日贡献补齐）

all(iterable) 只有所有元素都为真才返回 True；空序列返回 True（空真）。

```python
all([1, 2, 3])   # True
all([])          # True
all([1, 0, 3])   # False
```
