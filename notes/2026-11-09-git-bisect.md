# Git `bisect`：用二分法找出引入 bug 的那次提交

> Day 13 · 2026-11-09 · 📝 笔记

## 什么时候用

"上周还好好的，现在坏了，中间有几十个提交。" 一个个 checkout 太慢。`git bisect` 在"好的提交"和"坏的提交"之间做二分查找：每一步检出中间那个提交让你判断好坏，N 个提交最多约 log₂N 步就能定位（1000 个提交大约 10 步）。

## 手动流程

```bash
git bisect start
git bisect bad                 # 当前 HEAD 是坏的
git bisect good v1.2.0         # 这个标签/提交确认是好的
# Git 自动检出中间的提交，你测试后告诉它结果：
git bisect good                # 这个版本没问题
git bisect bad                 # 这个版本有问题
git bisect skip                # 这个版本没法测（编译不过等），跳过
# …重复，直到输出：<sha> is the first bad commit
git bisect reset               # 结束，回到开始前的分支
```

几个辅助命令：

- `git bisect log`：查看到目前为止的判断记录；`git bisect replay 文件` 可以重放。
- `git bisect visualize`（或 `view`）：看还剩哪些候选提交。
- 判断词可以自定义，适合找"性能变快的提交"这类不是 bug 的场景：`git bisect start --term-old=slow --term-new=fast`。

## 自动化：`git bisect run`

如果"好坏"能用一个命令判断，就让 Git 自己跑完全程。约定是看脚本的退出码：

| 退出码 | 含义 |
|---|---|
| `0` | good |
| `1`–`127`（`125` 除外） | bad |
| `125` | skip，这个版本无法测试 |
| 其他（如 `128+`） | 中止 bisect |

```bash
git bisect start HEAD v1.2.0          # 一步写好 bad 和 good
git bisect run python -m pytest tests/test_price.py -q
git bisect reset
```

测试脚本最好放在仓库**外面**（或用未跟踪的文件），否则检出旧提交时它可能不存在或是旧版本。

## 可运行的完整示例

下面的脚本在临时目录建一个仓库，做 20 次提交，其中第 13 次悄悄引入 bug，然后用 `bisect run` 自动找出它：

```bash
#!/usr/bin/env bash
set -euo pipefail
demo=$(mktemp -d) && cd "$demo"
git init -q && git config user.email demo@example.com && git config user.name demo

for i in $(seq 1 20); do
  if [ "$i" -ge 13 ]; then
    echo "def add(a, b): return a - b  # v$i" > calc.py   # bug 从第 13 次开始
  else
    echo "def add(a, b): return a + b  # v$i" > calc.py
  fi
  git add calc.py && git commit -qm "commit $i"
done

# 测试脚本放在仓库外，退出码 0 = good，1 = bad
cat > ../check_add.sh <<'SH'
python3 -B -c "from calc import add; assert add(2, 3) == 5"
SH

git bisect start HEAD "$(git rev-list --max-parents=0 HEAD)" > /dev/null  # HEAD 坏，首个提交好
git bisect run sh ../check_add.sh > ../bisect.log                      # 全程自动
git show -s --format='first bad commit: %h %s' refs/bisect/bad        # 结论
git bisect reset > /dev/null
```

输出（sha 每次不同）：

```text
first bad commit: 2a3fa12 commit 13
```

注意测试里用了 `python3 -B`（不写 `.pyc` 缓存）：bisect 频繁切换版本，文件在同一秒内被改写、大小又相同时，Python 可能误用旧的字节码缓存，导致判断错误。真实项目中也要警惕这类构建缓存，必要时在脚本里先清理。

完整的二分过程在 `../bisect.log` 里，20 个提交只测了 4～5 次。

## 小贴士

- 先确认"好"的那个点真的是好的，否则结果没意义。
- 一次只找一个问题；如果中间有别的不相关的故障，用 `skip` 或在脚本里返回 `125`。
- 合并提交多的历史可以加 `git bisect start --first-parent`，只沿主线二分，先定位是哪次合并引入的。
- 找到后用 `git show <sha>` 看改动，通常比读日志猜原因快得多。
- 忘了 `reset` 会停在分离 HEAD 状态，`git status` 会提示 "You are currently bisecting"。

参考：[git-bisect 官方文档](https://git-scm.com/docs/git-bisect)
