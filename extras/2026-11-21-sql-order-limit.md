# SQL ORDER BY + LIMIT：排序与分页

> 补记 · 2026-11-21（每日贡献补齐）

ORDER BY 排序（DESC 倒序），LIMIT 取前 N 条；分页用 LIMIT n OFFSET m，但数据量大时 OFFSET 会变慢。

```sql
SELECT * FROM posts ORDER BY created_at DESC LIMIT 10;
```
