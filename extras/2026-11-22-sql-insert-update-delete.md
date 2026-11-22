# SQL INSERT / UPDATE / DELETE：增删改

> 补记 · 2026-11-22（每日贡献补齐）

INSERT 加行，UPDATE 改行，DELETE 删行；UPDATE 和 DELETE 一定要带 WHERE，否则全表遭殃。

```sql
UPDATE users SET age = 19 WHERE id = 1;
DELETE FROM users WHERE id = 1;
```
