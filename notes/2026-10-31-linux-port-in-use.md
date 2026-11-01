# Linux 排查"端口被占用"：ss / lsof / fuser / kill

> 日期：2026-10-31 · 分类：Linux / 网络

启动服务时报 `OSError: [Errno 98] Address already in use`（或 Node 的 `EADDRINUSE`），说明这个端口已经有进程在 **监听（LISTEN）**。排查思路就三步：**找到谁占着 → 确认它是什么 → 决定停掉还是换端口**。

## 1. 找到占用端口的进程

### `ss`（首选，iproute2 自带，几乎所有发行版都有）

```bash
# -l 只看监听  -t TCP  -n 不解析域名/服务名  -p 显示进程
ss -ltnp 'sport = :8765'
```

输出示例：

```text
State  Recv-Q Send-Q Local Address:Port Peer Address:Port Process
LISTEN 0      5            0.0.0.0:8765      0.0.0.0:*    users:(("python3",pid=768682,fd=3))
```

- `users:(("python3",pid=...))` 就是答案。
- 看不到 `Process` 列？那是别的用户（比如 root）的进程，加 `sudo` 再跑。
- UDP 端口把 `-t` 换成 `-u`；全部监听端口：`ss -ltnp`。
- `ss` 是老命令 `netstat -tlnp` 的替代品，netstat 在新系统上常常没装。

### `lsof`（信息更全，但不一定预装）

```bash
lsof -iTCP:8765 -sTCP:LISTEN -nP
```

`-nP` 表示不解析主机名和端口名，速度快很多。没有就 `sudo apt install lsof`。

### `fuser`（只要 PID，适合脚本）

```bash
fuser 8765/tcp        # 输出：8765/tcp:  768682
```

## 2. 确认这个进程是什么

别急着杀，先看清楚是不是自己的东西：

```bash
ps -o pid,ppid,user,etime,cmd -p 768682
```

- `etime` 是运行了多久，`cmd` 是完整命令行。
- 如果是 systemd 服务（nginx、postgres 等），应该用 `sudo systemctl stop 服务名`，直接 kill 可能会被自动拉起。
- 如果是 Docker 容器映射出来的端口，`ss` 里看到的常是 `docker-proxy`，要用 `docker ps` 找容器再 `docker stop`。

## 3. 停掉它

```bash
kill 768682           # 默认发 SIGTERM，让进程优雅退出
kill -9 768682        # SIGKILL，强杀；只在 TERM 没反应时用
fuser -k 8765/tcp     # 一步到位：杀掉占用该端口的进程（默认 SIGKILL，慎用）
```

**先 TERM 后 KILL**：SIGTERM 给程序机会关闭连接、刷写文件；SIGKILL 无法被捕获，可能留下半写入的数据。

## 可直接运行的小实验

```bash
python3 -m http.server 8765 &          # 起一个占 8765 的服务
python3 -m http.server 8765            # 再起一个 → Address already in use
ss -ltnp 'sport = :8765'               # 找到第一个进程
kill %1                                # 结束后台任务
ss -ltn 'sport = :8765'                # 只剩表头，端口已释放
```

## 补充：刚关掉服务又起不来？

TCP 连接主动关闭的一方会进入 `TIME_WAIT`（通常持续约 60 秒），这期间可能仍然绑不上同一端口。用 `ss -tan state time-wait '( sport = :8765 )'` 能看到这些残留连接。自己写服务端时在 `bind` 前设置 `SO_REUSEADDR` 就能避免：

```python
import socket
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("0.0.0.0", 8765))
s.listen()
```

Python 标准库里 `http.server.HTTPServer` 已经设置了 `allow_reuse_address = True`；而基类 `socketserver.TCPServer` 默认是 `False`，自己继承时记得打开。

## 速记

| 想做什么 | 命令 |
|---|---|
| 谁在占端口 | `ss -ltnp 'sport = :端口'` |
| 只要 PID | `fuser 端口/tcp` |
| 看进程详情 | `ps -o pid,user,etime,cmd -p PID` |
| 优雅停止 | `kill PID` |
| 强制停止 | `kill -9 PID` |
