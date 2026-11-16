# Python getattr()：安全取属性

> 补记 · 2026-11-16（每日贡献补齐）

getattr(obj, name, default) 取属性，不存在时返回 default 而不是报错；配合 hasattr 做动态访问。

```python
getattr({"a": 1}, "get", None)  # dict 的 get 方法
getattr({}, "missing", "x")    # 'x'
```
