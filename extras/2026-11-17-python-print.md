# Python print()：sep / end / flush

> 补记 · 2026-11-17（每日贡献补齐）

print() 默认用空格分隔、用换行结尾；sep 改分隔符，end 改结尾，flush=True 立即刷出（日志、进度条常用）。

```python
print("a", "b", sep="-", end="!\n")  # a-b!
```
