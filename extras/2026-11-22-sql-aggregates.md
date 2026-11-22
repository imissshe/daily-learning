# SQL 聚合函数：COUNT / SUM / AVG

> 补记 · 2026-11-22（每日贡献补齐）

COUNT(*) 数所有行，COUNT(col) 只数该列非 NULL 的行；SUM/AVG 求和与均值，NULL 不参与计算。

```sql
SELECT COUNT(*), AVG(age) FROM users;
```
