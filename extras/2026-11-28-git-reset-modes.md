# Git reset 三种模式：soft / mixed / hard

> 补记 · 2026-11-28（每日贡献补齐）

--soft 只动 HEAD，改动留在暂存区；--mixed（默认）动 HEAD 和暂存区，改动回工作区；--hard 三者全丢弃，危险操作。

```bash
git reset --soft HEAD~1
git reset HEAD~1
```
