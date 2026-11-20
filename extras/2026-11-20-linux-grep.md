# Linux grep：文本搜索

> 补记 · 2026-11-20（每日贡献补齐）

grep -r 递归搜目录，-n 显示行号，-i 忽略大小写，--include 只搜特定类型的文件。

```bash
grep -rn "TODO" --include="*.py" .
```
