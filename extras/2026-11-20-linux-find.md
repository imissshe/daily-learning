# Linux find：按条件找文件

> 补记 · 2026-11-20（每日贡献补齐）

find 按名字、类型、时间找文件；-name 支持通配符，-mtime -7 是一周内改过的。

```bash
find . -name "*.log" -mtime -7
find . -type f -size +10M
```
