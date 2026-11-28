# Git bisect：二分定位坏提交

> 补记 · 2026-11-28（每日贡献补齐）

bisect 用二分法定位引入 bug 的提交：标记一个好的和一个坏的，中间每次二分测试，好坏反馈后自动缩小范围。

```bash
git bisect start
git bisect bad
git bisect good <commit>
```
