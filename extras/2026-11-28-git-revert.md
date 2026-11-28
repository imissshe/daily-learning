# Git revert：不改历史的反悔

> 补记 · 2026-11-28（每日贡献补齐）

git revert 生成一个新提交来撤销指定提交的改动，历史保持完整；已经推到远端的提交用 revert 而不是 reset。

```bash
git revert <commit>
```
