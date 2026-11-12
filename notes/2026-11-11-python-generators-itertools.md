# Python 生成器与 itertools：惰性求值处理大数据流（Day 15 · 2026-11-11）

## 为什么要用生成器

列表会把所有元素一次性放进内存；生成器（generator）是**惰性**的：要一个才算一个。
处理大文件、日志流、无限序列时，生成器能让内存占用保持 O(1)，而且可以像管道一样一段段串起来。

```python
import sys

nums_list = [i * i for i in range(1_000_000)]   # 列表推导：立刻算完 100 万个
nums_gen = (i * i for i in range(1_000_000))    # 生成器表达式：只是一个“配方”

print(sys.getsizeof(nums_list) > 1_000_000)  # True，约 8 MB
print(sys.getsizeof(nums_gen) < 1_000)       # True，只有两百字节左右
```

## yield：写自己的生成器函数

函数里出现 `yield` 就变成生成器函数。每次 `next()` 运行到下一个 `yield` 暂停，局部变量都保留着。

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

g = countdown(3)
print(next(g), next(g), next(g))  # 3 2 1
# 再 next(g) 会抛 StopIteration；for 循环会自动处理它
print(list(countdown(3)))         # [3, 2, 1]
```

> ⚠️ 生成器只能遍历**一次**。遍历完再 `list(g)` 得到的是空列表 `[]`。需要多次用就重新创建，或先 `list()` 存起来。

## 生成器管道：像 shell 的 `|` 一样串联

```python
lines = [
    "INFO start",
    "ERROR db timeout",
    "INFO ok",
    "ERROR disk full",
]

def read_lines(src):          # 真实场景里可以是 open("app.log")，文件对象本身就是惰性的
    for line in src:
        yield line.rstrip("\n")

def grep(pattern, rows):
    return (r for r in rows if pattern in r)

def take_message(rows):
    return (r.split(" ", 1)[1] for r in rows)

errors = take_message(grep("ERROR", read_lines(lines)))
print(list(errors))  # ['db timeout', 'disk full']
```

每一步只处理一行，几 GB 的日志也不会爆内存。

## yield from：把子生成器“转包”出去

```python
def flatten(nested):
    for item in nested:
        if isinstance(item, list):
            yield from flatten(item)   # 递归展开，比手写 for x in ...: yield x 简洁
        else:
            yield item

print(list(flatten([1, [2, [3, 4]], 5])))  # [1, 2, 3, 4, 5]
```

## itertools 常用工具

```python
from itertools import islice, count, chain, groupby, accumulate, batched  # batched 需要 Python 3.12+

print(list(islice(count(10), 3)))              # [10, 11, 12]  从无限序列里切前 3 个
print(list(chain([1, 2], (3, 4))))             # [1, 2, 3, 4]  首尾相接多个可迭代对象
print(list(accumulate([1, 2, 3, 4])))          # [1, 3, 6, 10] 前缀和
print(list(batched("abcdefg", 3)))             # [('a','b','c'), ('d','e','f'), ('g',)] 分批

# groupby 只合并“相邻”的相同 key，所以通常要先按同一个 key 排序
words = ["apple", "avocado", "banana", "blueberry", "cherry"]
for letter, grp in groupby(sorted(words), key=lambda w: w[0]):
    print(letter, list(grp))
# a ['apple', 'avocado']
# b ['banana', 'blueberry']
# c ['cherry']
```

Python 3.12 以下没有 `batched`，可以自己写：

```python
from itertools import islice

def batched_compat(iterable, n):
    it = iter(iterable)
    while chunk := tuple(islice(it, n)):
        yield chunk

print(list(batched_compat(range(5), 2)))  # [(0, 1), (2, 3), (4,)]
```

## 速记

| 场景 | 写法 |
|---|---|
| 只遍历一次、数据量大 | 生成器表达式 `(x for x in ...)` |
| 需要索引、多次遍历、`len()` | 列表 `[x for x in ...]` |
| 取前 N 个 | `islice(it, N)` |
| 拼接多个序列 | `chain(a, b)` / `chain.from_iterable(xs)` |
| 分组 | 先 `sorted(key=f)` 再 `groupby(key=f)` |
| 前缀和 / 累计 | `accumulate` |
| 分批调用 API | `batched(it, n)`（3.12+） |

还有一个小技巧：`sum(x * x for x in nums)`、`any(...)`、`max(...)` 直接接生成器表达式，不用多套一层方括号，`any` 找到第一个 True 就会提前停下。
