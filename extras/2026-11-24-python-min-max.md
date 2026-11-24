# Python min() / max()：带 key 与 default

> 补记 · 2026-11-24（每日贡献补齐）

min()/max() 可以传 key 函数按指定标准比较；空序列会报错，传 default 可以兜底。

```python
max(["bb", "a"], key=len)   # 'bb'
max([], default=0)          # 0
```
