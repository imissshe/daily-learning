# Python sys.argv：命令行参数

> 补记 · 2026-11-19（每日贡献补齐）

sys.argv 是命令行参数列表；argv[0] 是脚本自己的名字，真正的参数从 argv[1] 开始，都是字符串。

```python
import sys
print(sys.argv)  # 如 ['a.py', 'x', 'y']
```
