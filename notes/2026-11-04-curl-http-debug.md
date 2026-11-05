# 用 curl 调试 HTTP 请求速查

日常排查接口问题时，`curl` 是最直接的工具。下面是最常用的选项。

## 1. 看响应头和详细过程

```bash
curl -i https://httpbin.org/get      # 输出响应头 + 响应体
curl -I https://httpbin.org/get      # 只发 HEAD 请求，只看响应头
curl -v https://httpbin.org/get      # 详细模式：DNS、TLS 握手、请求头、响应头
```

`-v` 输出里 `>` 开头是发出去的请求，`<` 开头是收到的响应。

## 2. 发送 POST / JSON

```bash
curl -X POST https://httpbin.org/post \
  -H 'Content-Type: application/json' \
  -d '{"name": "chuan", "day": 9}'

# curl 7.82+ 可以用 --json，自动设置 Content-Type 和 Accept
curl --json '{"name": "chuan"}' https://httpbin.org/post

# 表单 / 文件上传
curl -F 'file=@README.md' https://httpbin.org/post
```

## 3. 只拿状态码和耗时

```bash
curl -s -o /dev/null -w '%{http_code}\n' https://httpbin.org/status/404

curl -s -o /dev/null -w 'dns=%{time_namelookup} connect=%{time_connect} tls=%{time_appconnect} ttfb=%{time_starttransfer} total=%{time_total}\n' https://example.com
```

`-s` 静默，`-o /dev/null` 丢弃响应体，`-w` 自定义输出格式。分段耗时能帮你判断慢在 DNS、建连还是服务端处理。

## 4. 重定向、超时、重试

```bash
curl -L https://httpbin.org/redirect/2          # 跟随 3xx 重定向
curl --max-time 5 --connect-timeout 2 URL        # 总超时 5 秒，建连超时 2 秒
curl --retry 3 --retry-delay 1 URL               # 失败重试
curl -f URL                                      # HTTP >= 400 时返回非 0 退出码，适合脚本
```

## 5. 认证与 Cookie

```bash
curl -u user:pass https://httpbin.org/basic-auth/user/pass
curl -H "Authorization: Bearer $TOKEN" URL
curl -c cookies.txt -b cookies.txt URL           # 保存并携带 cookie
```

## 6. 绕过 DNS 指定 IP（测试新服务器很有用）

```bash
curl --resolve example.com:443:93.184.215.14 https://example.com
```

## 小结

| 需求 | 选项 |
|---|---|
| 看头 | `-i` / `-I` / `-v` |
| 发 JSON | `--json` 或 `-H` + `-d` |
| 状态码/耗时 | `-s -o /dev/null -w` |
| 跟随跳转 | `-L` |
| 脚本里判断失败 | `-f`、`--max-time` |
| 指定解析 | `--resolve` |
