# Linux curl：调接口速查

> 补记 · 2026-11-21（每日贡献补齐）

curl 调 HTTP 接口：-X 指定方法，-H 加请求头，-d 发数据，-i 同时看响应头，-s 安静模式。

```bash
curl -s https://api.github.com/users/imissshe | head -c 200
curl -X POST -H "Content-Type: application/json" -d '{"a":1}' https://example.com/api
```
