# SQL SELECT + WHERE：查与过滤

> 补记 · 2026-11-21（每日贡献补齐）

SELECT 挑列，WHERE 过滤行；* 是全列，开发调试可以，大查询只拿需要的列更快。

```sql
SELECT name, age FROM users WHERE age >= 18;
```
