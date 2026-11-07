# Python `pathlib`：用对象代替字符串拼路径

> Day 10 · 2026-11-06 · 📝 笔记

## 为什么不用 `os.path`

`os.path.join("a", "b", "c.txt")` 返回字符串，后续还要再包一层才能判断、改后缀、列目录。`pathlib.Path` 把路径当成对象，拼接、查询、读写都挂在同一个类型上，跨平台分隔符也自动处理。

```python
from pathlib import Path

p = Path("data") / "raw" / "input.csv"
print(p)                 # data/raw/input.csv
print(p.name)            # input.csv
print(p.stem, p.suffix)  # input .csv
print(p.parent)          # data/raw
```

`/` 运算符就是拼接；不要用 `+` 拼字符串。

## 常用查询

```python
from pathlib import Path

here = Path(__file__).resolve().parent  # 当前脚本所在目录（绝对路径）

print(here.exists())
print(here.is_dir(), here.is_file())
print(list(here.glob("*.md")))          # 当前层匹配
print(list(here.rglob("*.py")))         # 递归匹配
```

`Path.cwd()` 是进程当前工作目录；`Path.home()` 是用户主目录。脚本里定位资源优先用 `__file__`，不要依赖你从哪启动。

## 读写文件

```python
from pathlib import Path

note = Path("/tmp/pathlib-demo.txt")
note.write_text("hello pathlib\n", encoding="utf-8")
print(note.read_text(encoding="utf-8"))

# 二进制
note.with_suffix(".bin").write_bytes(b"\x00\x01")
```

等价于 `open` + `read`/`write`，默认仍要显式传 `encoding="utf-8"`，避免本地默认编码踩坑。

## 创建、改名、换后缀

```python
from pathlib import Path

out = Path("/tmp/pathlib-out")
out.mkdir(parents=True, exist_ok=True)   # 类似 mkdir -p

src = out / "draft.txt"
src.write_text("v1", encoding="utf-8")

dst = src.with_name("final.txt")         # 同目录换文件名
src.rename(dst)

backup = dst.with_suffix(".txt.bak")     # 改后缀
dst.replace(backup)                     # 目标已存在也会覆盖（平台相关，写脚本前先确认）
print(backup.read_text(encoding="utf-8"))
```

`mkdir(parents=True, exist_ok=True)` 是建目录的默认安全写法；需要“目录已存在就报错”时再把 `exist_ok` 关掉。

## 遍历与过滤

```python
from pathlib import Path

root = Path("/tmp/pathlib-out")
for path in sorted(root.iterdir()):
    kind = "dir" if path.is_dir() else "file"
    print(f"{kind}: {path.name}")
```

只关心某类文件时用 `glob` / `rglob`，比自己递归再 `endswith` 清晰。

## 要点

- 新代码优先 `pathlib`；只有和老 API（只收 `str`）对接时才 `str(path)` 或 `os.fspath(path)`。
- 拼接用 `/`，不要 `os.path.join` 和 `Path` 混着拼。
- 读写文本始终带 `encoding="utf-8"`。
- 定位脚本旁的资源用 `Path(__file__).resolve().parent`，别用相对字符串赌 cwd。
