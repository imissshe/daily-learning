# Python split() / join()：切分与拼接互逆

> 补记 · 2026-11-26（每日贡献补齐）

split() 按分隔符切字符串，join() 用分隔符拼回去；split() 不带参数时按任意空白切，还会自动去掉首尾空白。

```python
"a,b,c".split(",")       # ['a', 'b', 'c']
"-".join(["a", "b"])     # 'a-b'
"  a  b ".split()        # ['a', 'b']
```
