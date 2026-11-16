# Python hasattr()：本质是试取属性

> 补记 · 2026-11-16（每日贡献补齐）

hasattr(obj, name) 本质是调用 getattr 并捕获异常；如果属性的 getter 本身抛异常，也会返回 False。

```python
hasattr("abc", "upper")  # True
hasattr("abc", "nope")   # False
```
