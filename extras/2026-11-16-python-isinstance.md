# Python isinstance()：类型判断

> 补记 · 2026-11-16（每日贡献补齐）

isinstance(x, 类型) 判断归属，支持传元组一次判多种类型；注意 bool 是 int 的子类。

```python
isinstance(True, int)        # True
isinstance(1, (int, float))  # True
```
