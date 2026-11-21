# Linux ps / top：看进程

> 补记 · 2026-11-21（每日贡献补齐）

ps aux 看全部进程，top 实时看资源占用；kill 发终止信号，kill -9 是强制杀（最后手段）。

```bash
ps aux | grep python
kill <pid>
```
