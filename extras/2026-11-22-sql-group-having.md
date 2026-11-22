# SQL GROUP BY + HAVING：分组后过滤

> 补记 · 2026-11-22（每日贡献补齐）

GROUP BY 按列分组聚合；WHERE 过滤的是分组前的行，HAVING 过滤的是分组后的结果。

```sql
SELECT city, COUNT(*) FROM users GROUP BY city HAVING COUNT(*) > 10;
```
