# Python json：dumps / loads 与中文

> 补记 · 2026-11-26（每日贡献补齐）

json.dumps() 转字符串，json.loads() 转回来；写中文时传 ensure_ascii=False，否则中文会被转成 \u 形式。

```python
import json
json.dumps({"名": "小明"}, ensure_ascii=False)  # '{"名": "小明"}'
```
