# Git checkout 与 switch / restore 的分工

> 补记 · 2026-11-19（每日贡献补齐）

新版 Git 建议分工：switch 切分支、restore 恢复文件；checkout 是老命令，两个活都能干但容易误操作。

```bash
git switch main
git restore --staged a.txt   # 取消暂存
git restore a.txt            # 丢弃工作区改动
```
