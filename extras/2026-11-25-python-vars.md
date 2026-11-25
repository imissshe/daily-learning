# Python vars()：对象的 __dict__

> 补记 · 2026-11-25（每日贡献补齐）

vars(obj) 返回对象的 __dict__（属性字典）；没有 __dict__ 的对象（如用了 __slots__ 的类）会报错。

```python
class C:
    def __init__(self): self.x = 1
vars(C())  # {'x': 1}
```
