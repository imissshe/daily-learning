# Python dataclasses 实战：少写样板代码的数据类

> Day 19 · 2026-11-15 · 📝 笔记

写一个"只装数据"的类时，手写 `__init__`、`__repr__`、`__eq__` 很啰嗦。标准库 `dataclasses`（Python 3.7+）用一个装饰器帮你自动生成这些方法。

## 1. 最小例子

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float = 0.0          # 有默认值的字段必须放在没有默认值的字段之后

p = Point(1.5)
print(p)                    # Point(x=1.5, y=0.0)  —— 自动 __repr__
assert p == Point(1.5, 0.0) # 自动 __eq__：按字段逐个比较
```

注意：类型注解只是"声明字段"，**运行时不做类型检查**，`Point("a")` 也能创建成功。

## 2. 可变默认值的坑：用 `field(default_factory=...)`

```python
from dataclasses import dataclass, field

@dataclass
class Cart:
    owner: str
    items: list[str] = field(default_factory=list)   # 每个实例一个新列表

a, b = Cart("a"), Cart("b")
a.items.append("apple")
assert b.items == []        # 互不影响
```

直接写 `items: list = []` 会在定义类时报 `ValueError: mutable default ... is not allowed`——dataclass 主动帮你拦住了"所有实例共享同一个列表"的经典 bug。

## 3. `__post_init__`：校验与派生字段

```python
from dataclasses import dataclass, field

@dataclass
class Rect:
    w: float
    h: float
    area: float = field(init=False)   # 不出现在 __init__ 参数里

    def __post_init__(self):
        if self.w < 0 or self.h < 0:
            raise ValueError("边长不能为负")
        self.area = self.w * self.h

assert Rect(2, 3).area == 6
try:
    Rect(-1, 2)
except ValueError as e:
    print("校验生效:", e)
```

## 4. 常用参数：`frozen`、`order`、`slots`

```python
from dataclasses import dataclass, FrozenInstanceError

@dataclass(frozen=True, order=True)
class Version:
    major: int
    minor: int
    patch: int = 0

v = Version(1, 2)
try:
    v.major = 2
except FrozenInstanceError:
    print("frozen：实例不可修改")

# frozen + eq 会自动生成 __hash__，可以放进 set / 当 dict 的 key
assert len({Version(1, 2), Version(1, 2, 0)}) == 1
# order=True 按字段顺序像元组一样比较
assert sorted([Version(1, 10), Version(1, 2, 5)]) == [Version(1, 2, 5), Version(1, 10)]
```

| 参数 | 作用 |
|---|---|
| `frozen=True` | 赋值会抛 `FrozenInstanceError`，适合配置、值对象 |
| `order=True` | 生成 `< <= > >=`，按字段定义顺序比较 |
| `slots=True`（3.10+） | 生成 `__slots__`，省内存、属性访问更快，不能随意加新属性 |
| `kw_only=True`（3.10+） | 所有字段只能用关键字传参，避免位置参数传错 |

## 5. 与 dict / 元组互转、复制修改

```python
from dataclasses import dataclass, asdict, astuple, replace

@dataclass(frozen=True)
class User:
    name: str
    age: int

u = User("chuan", 18)
assert asdict(u) == {"name": "chuan", "age": 18}   # 方便转 JSON
assert astuple(u) == ("chuan", 18)
u2 = replace(u, age=19)       # frozen 对象"修改"的正确姿势：生成新对象
assert u.age == 18 and u2.age == 19
```

`asdict` 会**递归**转换嵌套的 dataclass、list、dict。

## 6. 什么时候用什么？

- **dataclass**：普通数据容器、配置对象，首选。
- **`typing.NamedTuple`**：需要不可变 + 能像元组一样解包/索引时。
- **pydantic**（第三方）：数据来自外部（JSON、请求体），需要**运行时类型校验和转换**时。

## 小结

`@dataclass` 自动生成 `__init__ / __repr__ / __eq__`；可变默认值用 `default_factory`；校验写在 `__post_init__`；不可变用 `frozen=True` 配合 `replace()`。它不做运行时类型检查，这点要记牢。
