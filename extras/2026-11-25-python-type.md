# Python type()：查类型与动态建类

> 补记 · 2026-11-25（每日贡献补齐）

type(x) 返回对象的精确类型（不考虑继承，区别于 isinstance）；传三个参数可以动态创建一个类。

```python
type(1)          # <class 'int'>
type("C", (), {"x": 1})  # 动态创建一个类
```
