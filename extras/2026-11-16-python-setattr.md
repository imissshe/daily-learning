# Python setattr()：动态设属性

> 补记 · 2026-11-16（每日贡献补齐）

setattr(obj, name, value) 动态给对象设置属性，常用于按配置批量设值。

```python
class C: pass
c = C()
setattr(c, "x", 1)
c.x  # 1
```
