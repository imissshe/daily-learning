# 补记题库：每天贡献不够 10 次时，一篇笔记 = 一个提交。
# 每条都是独立的小知识点（Python / git / Linux / SQL / 正则），内容须真实可用。
BANK = [
    {
        "slug": "python-abs",
        "title": "Python abs()：绝对值与复数的模",
        "body": """abs(x) 返回 x 的绝对值；对复数返回模（到原点的距离）。

```python
abs(-3)        # 3
abs(3 + 4j)    # 5.0
```""",
    },
    {
        "slug": "python-all",
        "title": "Python all()：全部为真才为真",
        "body": """all(iterable) 只有所有元素都为真才返回 True；空序列返回 True（空真）。

```python
all([1, 2, 3])   # True
all([])          # True
all([1, 0, 3])   # False
```""",
    },
    {
        "slug": "python-any",
        "title": "Python any()：任一为真即为真",
        "body": """any(iterable) 只要有一个元素为真就返回 True；空序列返回 False。

```python
any([0, 0, 3])   # True
any([])          # False
```""",
    },
    {
        "slug": "python-enumerate",
        "title": "Python enumerate()：带下标遍历",
        "body": """enumerate() 同时拿到下标和元素；start 参数可以指定起始下标，不用自己维护计数器。

```python
for i, name in enumerate(["a", "b"], start=1):
    print(i, name)  # 1 a / 2 b
```""",
    },
    {
        "slug": "python-zip",
        "title": "Python zip()：并行遍历多个序列",
        "body": """zip() 把多个序列按位置配对，长度取最短的那个；zip(*rows) 可以用来转置二维表。

```python
list(zip([1, 2], ["a", "b"]))  # [(1, 'a'), (2, 'b')]
list(zip(*[[1, 2], [3, 4]]))   # [(1, 3), (2, 4)]
```""",
    },
    {
        "slug": "python-reversed",
        "title": "Python reversed()：反向迭代，不改原序列",
        "body": """reversed() 返回反向迭代器，不修改原序列；想拿列表要再包一层 list()。

```python
reversed([1, 2, 3])  # 迭代器，依次产出 3, 2, 1
list(reversed("abc"))  # ['c', 'b', 'a']
```""",
    },
    {
        "slug": "python-sorted",
        "title": "Python sorted()：key 与 reverse",
        "body": """sorted() 返回新列表，不改原序列；key 传函数决定排序依据，reverse=True 倒序。原地排序用 list.sort()。

```python
sorted(["bb", "a", "ccc"], key=len)  # ['a', 'bb', 'ccc']
```""",
    },
    {
        "slug": "python-sum",
        "title": "Python sum()：求和与起始值",
        "body": """sum() 对数字求和，start 参数指定起始值；浮点数求和精度要求高时用 math.fsum。

```python
sum([1, 2, 3])        # 6
sum([1, 2, 3], 10)    # 16
```""",
    },
    {
        "slug": "python-min-max",
        "title": "Python min() / max()：带 key 与 default",
        "body": """min()/max() 可以传 key 函数按指定标准比较；空序列会报错，传 default 可以兜底。

```python
max(["bb", "a"], key=len)   # 'bb'
max([], default=0)          # 0
```""",
    },
    {
        "slug": "python-filter",
        "title": "Python filter()：惰性筛选",
        "body": """filter(func, iterable) 只保留 func 返回真值的元素，是惰性的；func 传 None 时过滤掉所有假值。

```python
list(filter(None, [0, 1, "", "a"]))  # [1, 'a']
```""",
    },
    {
        "slug": "python-map",
        "title": "Python map()：惰性映射",
        "body": """map(func, iterable) 对每个元素应用函数，是惰性的；传多个序列时按最短的截断。

```python
list(map(str, [1, 2, 3]))  # ['1', '2', '3']
```""",
    },
    {
        "slug": "python-range",
        "title": "Python range()：半开区间，不占内存",
        "body": """range() 生成半开区间 [start, stop)，不实际建出列表，再大也不占内存；step 可以为负实现倒数。

```python
list(range(3))          # [0, 1, 2]
list(range(5, 0, -2))   # [5, 3, 1]
```""",
    },
    {
        "slug": "python-round",
        "title": "Python round()：银行家舍入",
        "body": """round() 对 .5 的情况按银行家舍入（取最近的偶数），不是四舍五入；要严格四舍五入用 decimal。

```python
round(2.5)  # 2
round(3.5)  # 4
```""",
    },
    {
        "slug": "python-divmod",
        "title": "Python divmod()：商和余数一次算出",
        "body": """divmod(a, b) 返回 (a // b, a % b)，一次算出商和余数，适合分页、进制换算这类场景。

```python
divmod(17, 5)  # (3, 2)
```""",
    },
    {
        "slug": "python-isinstance",
        "title": "Python isinstance()：类型判断",
        "body": """isinstance(x, 类型) 判断归属，支持传元组一次判多种类型；注意 bool 是 int 的子类。

```python
isinstance(True, int)        # True
isinstance(1, (int, float))  # True
```""",
    },
    {
        "slug": "python-getattr",
        "title": "Python getattr()：安全取属性",
        "body": """getattr(obj, name, default) 取属性，不存在时返回 default 而不是报错；配合 hasattr 做动态访问。

```python
getattr({"a": 1}, "get", None)  # dict 的 get 方法
getattr({}, "missing", "x")    # 'x'
```""",
    },
    {
        "slug": "python-setattr",
        "title": "Python setattr()：动态设属性",
        "body": """setattr(obj, name, value) 动态给对象设置属性，常用于按配置批量设值。

```python
class C: pass
c = C()
setattr(c, "x", 1)
c.x  # 1
```""",
    },
    {
        "slug": "python-hasattr",
        "title": "Python hasattr()：本质是试取属性",
        "body": """hasattr(obj, name) 本质是调用 getattr 并捕获异常；如果属性的 getter 本身抛异常，也会返回 False。

```python
hasattr("abc", "upper")  # True
hasattr("abc", "nope")   # False
```""",
    },
    {
        "slug": "python-vars",
        "title": "Python vars()：对象的 __dict__",
        "body": """vars(obj) 返回对象的 __dict__（属性字典）；没有 __dict__ 的对象（如用了 __slots__ 的类）会报错。

```python
class C:
    def __init__(self): self.x = 1
vars(C())  # {'x': 1}
```""",
    },
    {
        "slug": "python-id",
        "title": "Python id()：对象身份",
        "body": """id() 返回对象的唯一标识（CPython 里是内存地址）；is 比较的就是 id 是否相同。小整数和短字符串会被缓存复用。

```python
a = 256
b = 256
a is b  # True（小整数缓存）
```""",
    },
    {
        "slug": "python-type",
        "title": "Python type()：查类型与动态建类",
        "body": """type(x) 返回对象的精确类型（不考虑继承，区别于 isinstance）；传三个参数可以动态创建一个类。

```python
type(1)          # <class 'int'>
type("C", (), {"x": 1})  # 动态创建一个类
```""",
    },
    {
        "slug": "python-chr-ord",
        "title": "Python chr() / ord()：字符与码点互转",
        "body": """ord() 把单个字符转成 Unicode 码点，chr() 反向转回；ord 只接受长度为 1 的字符串。

```python
ord("A")  # 65
chr(97)   # 'a'
```""",
    },
    {
        "slug": "python-bin-hex-oct",
        "title": "Python bin() / hex() / oct()：进制转换",
        "body": """bin()/hex()/oct() 把整数转成二、十六、八进制字符串（带前缀）；反向用 int(x, base)。

```python
bin(10)       # '0b1010'
int("ff", 16)  # 255
```""",
    },
    {
        "slug": "python-format",
        "title": "Python format()：格式化数字与对齐",
        "body": """format() 与 f-string 共用一套格式语法：:.2f 保留两位小数、:>10 右对齐、:, 千分位分隔。

```python
f"{1234567:,}"   # '1,234,567'
f"{3.14159:.2f}"  # '3.14'
```""",
    },
    {
        "slug": "python-print",
        "title": "Python print()：sep / end / flush",
        "body": """print() 默认用空格分隔、用换行结尾；sep 改分隔符，end 改结尾，flush=True 立即刷出（日志、进度条常用）。

```python
print("a", "b", sep="-", end="!\\n")  # a-b!
```""",
    },
    {
        "slug": "python-input",
        "title": "Python input()：读一行，总返回字符串",
        "body": """input() 读一行输入，返回值永远是字符串，需要数字要自己转 int()/float()，并处理可能的 ValueError。

```python
n = int(input("请输入数字："))
```""",
    },
    {
        "slug": "python-open",
        "title": "Python open()：with 与编码",
        "body": """open() 配合 with 语句用完自动关闭文件；读写文本时显式指定 encoding="utf-8"，避免跨平台乱码。

```python
with open("a.txt", encoding="utf-8") as f:
    text = f.read()
```""",
    },
    {
        "slug": "python-len",
        "title": "Python len()：容器长度",
        "body": """len() 返回容器元素个数；自定义类实现 __len__ 方法后也能用 len()，返回的必须是大于等于 0 的整数。

```python
len("hello")  # 5
len([1, 2])   # 2
```""",
    },
    {
        "slug": "python-comprehension",
        "title": "Python 推导式：列表 / 字典 / 集合",
        "body": """推导式一行写出转换与筛选；字典推导式用 {k: v ...}，集合推导式用 {x ...}，生成器表达式用圆括号。

```python
[x * x for x in range(5) if x % 2 == 0]  # [0, 4, 16]
{k: v for k, v in [("a", 1)]}           # {'a': 1}
```""",
    },
    {
        "slug": "python-str-split-join",
        "title": "Python split() / join()：切分与拼接互逆",
        "body": """split() 按分隔符切字符串，join() 用分隔符拼回去；split() 不带参数时按任意空白切，还会自动去掉首尾空白。

```python
"a,b,c".split(",")       # ['a', 'b', 'c']
"-".join(["a", "b"])     # 'a-b'
"  a  b ".split()        # ['a', 'b']
```""",
    },
    {
        "slug": "python-json",
        "title": "Python json：dumps / loads 与中文",
        "body": """json.dumps() 转字符串，json.loads() 转回来；写中文时传 ensure_ascii=False，否则中文会被转成 \\u 形式。

```python
import json
json.dumps({"名": "小明"}, ensure_ascii=False)  # '{"名": "小明"}'
```""",
    },
    {
        "slug": "python-datetime",
        "title": "Python datetime：现在时间与日期",
        "body": """datetime.now() 取当前时间，date.today() 取今天日期；涉及时区要带 tzinfo，否则是“天真时间”，跨时区会算错。

```python
from datetime import date, datetime
date.today()            # 如 date(2026, 11, 15)
datetime.now().strftime("%Y-%m-%d %H:%M")
```""",
    },
    {
        "slug": "python-pathlib",
        "title": "Python pathlib：用对象代替字符串拼路径",
        "body": """Path 对象用 / 拼接路径，比字符串拼接直观；exists()、read_text()、glob() 都可以直接调。

```python
from pathlib import Path
p = Path("notes") / "2026-11-15.md"
p.exists()
```""",
    },
    {
        "slug": "python-counter",
        "title": "Python Counter：计数与 most_common",
        "body": """collections.Counter 统计元素出现次数；most_common(n) 取出频率最高的前 n 个。

```python
from collections import Counter
Counter("abracadabra").most_common(2)  # [('a', 5), ('b', 2)]
```""",
    },
    {
        "slug": "python-defaultdict",
        "title": "Python defaultdict：免判 key 是否存在",
        "body": """collections.defaultdict 访问不存在的 key 时自动用工厂函数建默认值，写分组、计数代码时不用先判断 key 在不在。

```python
from collections import defaultdict
d = defaultdict(list)
d["a"].append(1)  # {'a': [1]}
```""",
    },
    {
        "slug": "python-itertools-chain",
        "title": "Python itertools.chain：连接多个可迭代对象",
        "body": """chain() 把多个可迭代对象首尾相接成一个惰性序列，不用先拼成大列表。

```python
from itertools import chain
list(chain([1, 2], [3, 4]))  # [1, 2, 3, 4]
```""",
    },
    {
        "slug": "python-itertools-groupby",
        "title": "Python itertools.groupby：分组前要先排序",
        "body": """groupby() 按 key 把连续相同的元素分到一组；输入必须先按同一 key 排好序，否则相同 key 会被拆成多组。

```python
from itertools import groupby
data = sorted([("a", 1), ("b", 2), ("a", 3)], key=lambda x: x[0])
{k: list(v) for k, v in groupby(data, key=lambda x: x[0])}
```""",
    },
    {
        "slug": "python-random",
        "title": "Python random：choice / sample / shuffle",
        "body": """random.choice() 随机取一个，sample() 无放回取 k 个，shuffle() 原地打乱；需要可复现时先 seed()。

```python
import random
random.sample(range(10), 3)  # 如 [2, 7, 4]
```""",
    },
    {
        "slug": "python-math",
        "title": "Python math：gcd / isqrt / isclose",
        "body": """math.gcd() 最大公约数，math.isqrt() 整数平方根；浮点数不要用 == 比较，用 math.isclose()。

```python
import math
math.gcd(12, 18)              # 6
math.isclose(0.1 + 0.2, 0.3)  # True
```""",
    },
    {
        "slug": "python-re-search",
        "title": "Python re：search / match / fullmatch",
        "body": """re.search() 在全文里找，re.match() 只从开头找，re.fullmatch() 要求整个字符串都匹配；校验格式用 fullmatch 最稳。

```python
import re
re.fullmatch(r"\\d+", "123")   # 匹配
re.fullmatch(r"\\d+", "12a")   # 不匹配
```""",
    },
    {
        "slug": "python-os-environ",
        "title": "Python os.environ：读环境变量",
        "body": """os.environ 读环境变量；用 getenv(key, default) 可以带默认值，避免 key 不存在时抛 KeyError。

```python
import os
os.getenv("HOME", "/tmp")
```""",
    },
    {
        "slug": "python-sys-argv",
        "title": "Python sys.argv：命令行参数",
        "body": """sys.argv 是命令行参数列表；argv[0] 是脚本自己的名字，真正的参数从 argv[1] 开始，都是字符串。

```python
import sys
print(sys.argv)  # 如 ['a.py', 'x', 'y']
```""",
    },
    {
        "slug": "git-status",
        "title": "Git git status：先看状态再动手",
        "body": """git status 看工作区状态：哪些文件改了、哪些已暂存、哪些未跟踪；动手提交前先看一眼能少踩很多坑。

```bash
git status
git status --short   # 简洁版
```""",
    },
    {
        "slug": "git-diff",
        "title": "Git git diff：看改了什么",
        "body": """git diff 看工作区相对暂存区的改动，git diff --staged 看暂存区相对上次提交的改动；提交前过一遍 diff 是好习惯。

```bash
git diff
git diff --staged
```""",
    },
    {
        "slug": "git-log-oneline",
        "title": "Git git log：简洁看历史",
        "body": """git log --oneline --graph 一行一个提交加分支图；--all 看所有分支，-n 限制条数。

```bash
git log --oneline --graph -10
```""",
    },
    {
        "slug": "git-branch",
        "title": "Git git branch：分支的增删查",
        "body": """git branch 列出本地分支；git branch <名> 新建，git branch -d <名> 删除已合并的分支，-D 强制删。

```bash
git branch
git branch feature-x
```""",
    },
    {
        "slug": "git-checkout-switch",
        "title": "Git checkout 与 switch / restore 的分工",
        "body": """新版 Git 建议分工：switch 切分支、restore 恢复文件；checkout 是老命令，两个活都能干但容易误操作。

```bash
git switch main
git restore --staged a.txt   # 取消暂存
git restore a.txt            # 丢弃工作区改动
```""",
    },
    {
        "slug": "git-stash",
        "title": "Git git stash：临时收起改动",
        "body": """git stash 把没提交的改动临时收起来，工作区恢复干净；stash pop 恢复出来，stash list 看收了几份。

```bash
git stash
git stash pop
```""",
    },
    {
        "slug": "git-reset-modes",
        "title": "Git reset 三种模式：soft / mixed / hard",
        "body": """--soft 只动 HEAD，改动留在暂存区；--mixed（默认）动 HEAD 和暂存区，改动回工作区；--hard 三者全丢弃，危险操作。

```bash
git reset --soft HEAD~1
git reset HEAD~1
```""",
    },
    {
        "slug": "git-revert",
        "title": "Git revert：不改历史的反悔",
        "body": """git revert 生成一个新提交来撤销指定提交的改动，历史保持完整；已经推到远端的提交用 revert 而不是 reset。

```bash
git revert <commit>
```""",
    },
    {
        "slug": "git-merge-rebase",
        "title": "Git merge 与 rebase：分叉与拉直",
        "body": """merge 会留下一个合并提交和分叉历史；rebase 把提交一个个挪到目标分支顶端，历史是直线。公共分支不要 rebase。

```bash
git merge feature-x
git rebase main
```""",
    },
    {
        "slug": "git-cherry-pick",
        "title": "Git cherry-pick：只挑一个提交",
        "body": """cherry-pick 把某个提交单独复制到当前分支，适合只合一个修复、不合整个分支的场景。

```bash
git cherry-pick <commit>
```""",
    },
    {
        "slug": "git-remote-fetch-pull",
        "title": "Git remote / fetch / pull 的区别",
        "body": """fetch 只把远端更新下载到本地，不改工作区；pull = fetch + merge，会直接合进来；push 是把本地推上去。

```bash
git remote -v
git fetch
git pull
```""",
    },
    {
        "slug": "git-tag",
        "title": "Git tag：给提交打版本",
        "body": """tag 给某个提交打版本号；-a 是附注标签（带说明和打标人），轻量标签只有一个名字；推标签要加 --tags。

```bash
git tag -a v1.0 -m "first release"
git push --tags
```""",
    },
    {
        "slug": "git-blame",
        "title": "Git blame：这行是谁改的",
        "body": """git blame 看文件每一行最后是谁、在哪次提交改的；追查 bug 来源、问“这行为什么这样写”时最常用。

```bash
git blame README.md
```""",
    },
    {
        "slug": "git-bisect",
        "title": "Git bisect：二分定位坏提交",
        "body": """bisect 用二分法定位引入 bug 的提交：标记一个好的和一个坏的，中间每次二分测试，好坏反馈后自动缩小范围。

```bash
git bisect start
git bisect bad
git bisect good <commit>
```""",
    },
    {
        "slug": "git-reflog",
        "title": "Git reflog：找回误删的提交",
        "body": """reflog 记录 HEAD 的每一次移动；reset 错了、分支删错了，都能从 reflog 里找到提交哈希再恢复。

```bash
git reflog
git reset --hard <hash>
```""",
    },
    {
        "slug": "linux-ls",
        "title": "Linux ls：列文件常用选项",
        "body": """ls -la 看隐藏文件和权限，-lh 人性化显示大小，-t 按修改时间排序，-S 按大小排序。

```bash
ls -lah
ls -lt
```""",
    },
    {
        "slug": "linux-grep",
        "title": "Linux grep：文本搜索",
        "body": """grep -r 递归搜目录，-n 显示行号，-i 忽略大小写，--include 只搜特定类型的文件。

```bash
grep -rn "TODO" --include="*.py" .
```""",
    },
    {
        "slug": "linux-find",
        "title": "Linux find：按条件找文件",
        "body": """find 按名字、类型、时间找文件；-name 支持通配符，-mtime -7 是一周内改过的。

```bash
find . -name "*.log" -mtime -7
find . -type f -size +10M
```""",
    },
    {
        "slug": "linux-sed",
        "title": "Linux sed：流式替换文本",
        "body": """sed 's/旧/新/g' 替换每行所有匹配；-i 直接改文件（先备份更稳），-n '10,20p' 只打印指定行。

```bash
sed 's/foo/bar/g' a.txt
sed -n '10,20p' a.txt
```""",
    },
    {
        "slug": "linux-awk",
        "title": "Linux awk：按列处理文本",
        "body": """awk 按列处理文本：$1 是第一列，NF 是列数，NR 是行号；适合从命令输出里抽字段。

```bash
ps aux | awk '{print $2, $11}' | head
echo "a b c" | awk '{print $2}'
```""",
    },
    {
        "slug": "linux-curl",
        "title": "Linux curl：调接口速查",
        "body": """curl 调 HTTP 接口：-X 指定方法，-H 加请求头，-d 发数据，-i 同时看响应头，-s 安静模式。

```bash
curl -s https://api.github.com/users/imissshe | head -c 200
curl -X POST -H "Content-Type: application/json" -d '{"a":1}' https://example.com/api
```""",
    },
    {
        "slug": "linux-tar",
        "title": "Linux tar：打包与解包",
        "body": """tar -czf 打 gzip 包，-xzf 解 gzip 包，-tf 只看包里有什么不解开；记住 czf 是压、xzf 是解。

```bash
tar -czf backup.tar.gz notes/
tar -xzf backup.tar.gz
```""",
    },
    {
        "slug": "linux-ps-top",
        "title": "Linux ps / top：看进程",
        "body": """ps aux 看全部进程，top 实时看资源占用；kill 发终止信号，kill -9 是强制杀（最后手段）。

```bash
ps aux | grep python
kill <pid>
```""",
    },
    {
        "slug": "linux-ssh",
        "title": "Linux ssh：连服务器",
        "body": """ssh user@host 连远程服务器；-i 指定密钥文件，-p 指定端口；第一次连会让确认主机指纹。

```bash
ssh -i ~/.ssh/id_ed25519 user@host
ssh -p 2222 user@host
```""",
    },
    {
        "slug": "linux-df-du",
        "title": "Linux df / du：磁盘用量",
        "body": """df -h 看各磁盘分区剩余空间，du -sh 看某个目录占了多少；磁盘满了先从这两条命令找原因。

```bash
df -h
du -sh ~/workspace/*
```""",
    },
    {
        "slug": "sql-select-where",
        "title": "SQL SELECT + WHERE：查与过滤",
        "body": """SELECT 挑列，WHERE 过滤行；* 是全列，开发调试可以，大查询只拿需要的列更快。

```sql
SELECT name, age FROM users WHERE age >= 18;
```""",
    },
    {
        "slug": "sql-order-limit",
        "title": "SQL ORDER BY + LIMIT：排序与分页",
        "body": """ORDER BY 排序（DESC 倒序），LIMIT 取前 N 条；分页用 LIMIT n OFFSET m，但数据量大时 OFFSET 会变慢。

```sql
SELECT * FROM posts ORDER BY created_at DESC LIMIT 10;
```""",
    },
    {
        "slug": "sql-join",
        "title": "SQL JOIN：内连接与左连接",
        "body": """INNER JOIN 只保留两边都匹配的行；LEFT JOIN 保留左表全部行，右表没匹配的补 NULL。

```sql
SELECT u.name, o.amount
FROM users u LEFT JOIN orders o ON o.user_id = u.id;
```""",
    },
    {
        "slug": "sql-group-having",
        "title": "SQL GROUP BY + HAVING：分组后过滤",
        "body": """GROUP BY 按列分组聚合；WHERE 过滤的是分组前的行，HAVING 过滤的是分组后的结果。

```sql
SELECT city, COUNT(*) FROM users GROUP BY city HAVING COUNT(*) > 10;
```""",
    },
    {
        "slug": "sql-distinct",
        "title": "SQL DISTINCT：去重",
        "body": """DISTINCT 去掉结果里完全重复的行；只对 SELECT 的全部列组合去重，不是单列去重。

```sql
SELECT DISTINCT city FROM users;
```""",
    },
    {
        "slug": "sql-like",
        "title": "SQL LIKE：模糊匹配",
        "body": """LIKE 做模糊匹配：% 匹配任意多个字符，_ 匹配一个字符；大数据量下 LIKE '%x%' 走不了索引。

```sql
SELECT * FROM users WHERE name LIKE '张%';
```""",
    },
    {
        "slug": "sql-insert-update-delete",
        "title": "SQL INSERT / UPDATE / DELETE：增删改",
        "body": """INSERT 加行，UPDATE 改行，DELETE 删行；UPDATE 和 DELETE 一定要带 WHERE，否则全表遭殃。

```sql
UPDATE users SET age = 19 WHERE id = 1;
DELETE FROM users WHERE id = 1;
```""",
    },
    {
        "slug": "sql-aggregates",
        "title": "SQL 聚合函数：COUNT / SUM / AVG",
        "body": """COUNT(*) 数所有行，COUNT(col) 只数该列非 NULL 的行；SUM/AVG 求和与均值，NULL 不参与计算。

```sql
SELECT COUNT(*), AVG(age) FROM users;
```""",
    },
    {
        "slug": "regex-dot-star",
        "title": "正则 . 与 *：任意字符与零或多次",
        "body": """. 匹配除换行外任意一个字符，* 表示前面的内容出现零次或多次；.* 连用就是“任意长度的任意内容”。

```python
import re
re.search(r"a.*b", "axxb")  # 匹配
```""",
    },
    {
        "slug": "regex-plus-question",
        "title": "正则 + 与 ?：至少一次与零或一次",
        "body": """+ 表示前面的内容至少出现一次，? 表示零次或一次；\\d+ 就是“一位以上数字”，https? 能同时匹配 http 与 https。

```python
import re
re.fullmatch(r"\\d+", "123")  # 匹配
```""",
    },
    {
        "slug": "regex-anchors",
        "title": "正则 ^ 与 $：开头与结尾",
        "body": """^ 锚定开头，$ 锚定结尾；校验格式时两者配合才能保证整个字符串符合要求，而不是其中一段符合。

```python
import re
re.search(r"^abc", "xabc")  # 不匹配
re.search(r"abc$", "xabc")  # 匹配
```""",
    },
    {
        "slug": "regex-classes",
        "title": "正则字符类：[0-9] / \\d / \\w / \\s",
        "body": """[0-9] 匹配一位数字，等价于 \\d；\\w 匹配字母数字下划线，\\s 匹配空白；方括号里加 ^ 表示“除了这些”。

```python
import re
re.findall(r"\\d+", "a1b22")  # ['1', '22']
```""",
    },
    {
        "slug": "regex-groups",
        "title": "正则分组 () 与反向引用",
        "body": """() 把一部分括起来做分组，可以整体加量词，也可以在替换时用 \\1、\\2 引用；(?:...) 是不捕获的分组。

```python
import re
re.sub(r"(\\w+)@(\\w+)", r"\\2@\\1", "a@b")  # 'b@a'
```""",
    },
    {
        "slug": "regex-greedy-lazy",
        "title": "正则贪婪与懒惰量词",
        "body": """量词默认贪婪（尽量多匹配），后面加 ? 变懒惰（尽量少匹配）；从 HTML 里取标签内容时懒惰模式更常用。

```python
import re
re.search(r"<.+>", "<a><b>")    # 贪婪：'<a><b>'
re.search(r"<.+?>", "<a><b>")   # 懒惰：'<a>'
```""",
    },
    {
        "slug": "regex-alternation",
        "title": "正则 |：二选一",
        "body": """| 表示左右二选一；注意它的优先级最低，想限制范围要用括号括起来，如 (ab|cd)。

```python
import re
re.fullmatch(r"cat|dog", "dog")  # 匹配
```""",
    },
    {
        "slug": "regex-flags",
        "title": "正则 flags：re.I 与 re.M",
        "body": """re.I 忽略大小写，re.M 让 ^ 和 $ 匹配每一行的开头结尾（而不只是整个字符串的开头结尾）。

```python
import re
re.search(r"^b", "a\\nb", re.M)  # 匹配
re.fullmatch(r"abc", "ABC", re.I)  # 匹配
```""",
    },
]
