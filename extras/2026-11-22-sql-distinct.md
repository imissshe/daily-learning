# SQL DISTINCT：去重

> 补记 · 2026-11-22（每日贡献补齐）

DISTINCT 去掉结果里完全重复的行；只对 SELECT 的全部列组合去重，不是单列去重。

```sql
SELECT DISTINCT city FROM users;
```
