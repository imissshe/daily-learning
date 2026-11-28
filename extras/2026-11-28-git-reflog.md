# Git reflog：找回误删的提交

> 补记 · 2026-11-28（每日贡献补齐）

reflog 记录 HEAD 的每一次移动；reset 错了、分支删错了，都能从 reflog 里找到提交哈希再恢复。

```bash
git reflog
git reset --hard <hash>
```
