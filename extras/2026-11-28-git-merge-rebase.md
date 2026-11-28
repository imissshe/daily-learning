# Git merge 与 rebase：分叉与拉直

> 补记 · 2026-11-28（每日贡献补齐）

merge 会留下一个合并提交和分叉历史；rebase 把提交一个个挪到目标分支顶端，历史是直线。公共分支不要 rebase。

```bash
git merge feature-x
git rebase main
```
