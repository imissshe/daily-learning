# Python enumerate()：带下标遍历

> 补记 · 2026-11-23（每日贡献补齐）

enumerate() 同时拿到下标和元素；start 参数可以指定起始下标，不用自己维护计数器。

```python
for i, name in enumerate(["a", "b"], start=1):
    print(i, name)  # 1 a / 2 b
```
