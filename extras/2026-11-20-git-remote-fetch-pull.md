# Git remote / fetch / pull 的区别

> 补记 · 2026-11-20（每日贡献补齐）

fetch 只把远端更新下载到本地，不改工作区；pull = fetch + merge，会直接合进来；push 是把本地推上去。

```bash
git remote -v
git fetch
git pull
```
