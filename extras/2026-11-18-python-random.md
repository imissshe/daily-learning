# Python random：choice / sample / shuffle

> 补记 · 2026-11-18（每日贡献补齐）

random.choice() 随机取一个，sample() 无放回取 k 个，shuffle() 原地打乱；需要可复现时先 seed()。

```python
import random
random.sample(range(10), 3)  # 如 [2, 7, 4]
```
