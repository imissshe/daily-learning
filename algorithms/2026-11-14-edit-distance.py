"""
编辑距离 Edit Distance (Day 18 · 2026-11-14)

题目（自己的话）：
给两个字符串 a 和 b。每一步可以对 a 做三种操作之一：
插入一个字符、删除一个字符、把一个字符替换成另一个字符。
问把 a 变成 b 最少需要几步？

思路（二维动态规划）：
定义 dp[i][j] = 把 a 的前 i 个字符变成 b 的前 j 个字符的最少步数。
- 边界：dp[i][0] = i（全删掉），dp[0][j] = j（全插入）。
- 转移：看最后一个字符 a[i-1] 和 b[j-1]：
  * 相等：不用操作，dp[i][j] = dp[i-1][j-1]
  * 不等：取三种操作里最小的再 +1
      - 替换 a[i-1] -> b[j-1]：dp[i-1][j-1] + 1
      - 删除 a[i-1]：          dp[i-1][j]   + 1
      - 插入 b[j-1]：          dp[i][j-1]   + 1
- 答案：dp[len(a)][len(b)]。

空间优化：dp[i][*] 只依赖上一行和本行左边，所以可以滚动成一维数组，
用变量 prev_diag 保存“左上角” dp[i-1][j-1] 的旧值。
另外让较短的字符串当列，空间降到 O(min(m, n))。

额外：回溯 dp 表还原出具体的操作序列，并验证这些操作真的能把 a 变成 b。
对照解法：带记忆化的递归（从前往后比较），用随机小字符串交叉校验。

复杂度（m = len(a), n = len(b)）：
- 二维 DP：时间 O(m·n)，空间 O(m·n)
- 一维滚动：时间 O(m·n)，空间 O(min(m, n))
"""
import random
from functools import lru_cache
from typing import List, Tuple


def edit_distance_table(a: str, b: str) -> List[List[int]]:
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
    return dp


def edit_distance(a: str, b: str) -> int:
    """一维滚动数组版本，空间 O(min(m, n))。编辑距离对称，可交换 a、b。"""
    if len(a) < len(b):
        a, b = b, a
    n = len(b)
    row = list(range(n + 1))  # dp[0][*]
    for i in range(1, len(a) + 1):
        prev_diag = row[0]  # dp[i-1][0]
        row[0] = i
        for j in range(1, n + 1):
            tmp = row[j]  # dp[i-1][j]，稍后成为下一格的“左上角”
            if a[i - 1] == b[j - 1]:
                row[j] = prev_diag
            else:
                row[j] = 1 + min(prev_diag, row[j], row[j - 1])
            prev_diag = tmp
    return row[n]


def edit_ops(a: str, b: str) -> List[Tuple[str, int, str]]:
    """从 dp 表右下角回溯，返回操作列表 (op, 位置, 字符)，按从左到右执行。"""
    dp = edit_distance_table(a, b)
    i, j = len(a), len(b)
    ops: List[Tuple[str, int, str]] = []
    while i > 0 or j > 0:
        if i > 0 and j > 0 and a[i - 1] == b[j - 1] and dp[i][j] == dp[i - 1][j - 1]:
            i, j = i - 1, j - 1
        elif i > 0 and j > 0 and dp[i][j] == dp[i - 1][j - 1] + 1:
            ops.append(("replace", i - 1, b[j - 1]))
            i, j = i - 1, j - 1
        elif i > 0 and dp[i][j] == dp[i - 1][j] + 1:
            ops.append(("delete", i - 1, a[i - 1]))
            i -= 1
        else:
            ops.append(("insert", i, b[j - 1]))
            j -= 1
    # 回溯得到的是从右往左的操作；从右往左执行时下标不会互相影响
    return ops


def apply_ops(a: str, ops: List[Tuple[str, int, str]]) -> str:
    s = list(a)
    for op, pos, ch in ops:  # ops 已是从右往左的顺序
        if op == "replace":
            s[pos] = ch
        elif op == "delete":
            del s[pos]
        else:
            s.insert(pos, ch)
    return "".join(s)


def edit_distance_memo(a: str, b: str) -> int:
    @lru_cache(maxsize=None)
    def go(i: int, j: int) -> int:
        if i == len(a):
            return len(b) - j
        if j == len(b):
            return len(a) - i
        if a[i] == b[j]:
            return go(i + 1, j + 1)
        return 1 + min(go(i + 1, j + 1), go(i + 1, j), go(i, j + 1))

    return go(0, 0)


if __name__ == "__main__":
    assert edit_distance("horse", "ros") == 3
    assert edit_distance("intention", "execution") == 5
    assert edit_distance("", "") == 0
    assert edit_distance("abc", "") == 3
    assert edit_distance("", "xyz") == 3
    assert edit_distance("kitten", "sitting") == 3
    assert edit_distance("same", "same") == 0
    assert edit_distance_table("horse", "ros")[5][3] == 3

    for a, b in [("horse", "ros"), ("intention", "execution"), ("", "ab"), ("ab", "")]:
        ops = edit_ops(a, b)
        assert len(ops) == edit_distance(a, b)
        assert apply_ops(a, ops) == b

    rng = random.Random(2026)
    for _ in range(500):
        a = "".join(rng.choice("abc") for _ in range(rng.randint(0, 8)))
        b = "".join(rng.choice("abc") for _ in range(rng.randint(0, 8)))
        d = edit_distance(a, b)
        assert d == edit_distance_memo(a, b) == edit_distance_table(a, b)[len(a)][len(b)]
        assert d == edit_distance(b, a)  # 对称性
        ops = edit_ops(a, b)
        assert len(ops) == d and apply_ops(a, ops) == b

    print("all tests passed ✅")
