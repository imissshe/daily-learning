"""
2026-10-30 · 无重复字符的最长子串 / Longest Substring Without Repeating Characters

题目（自己的话）
----------------
给一个字符串 s，找出其中**连续**的一段子串，要求这段里没有任何字符重复出现，
返回满足条件的最长子串的长度。空字符串的答案是 0。

Problem (in my own words)
-------------------------
Given a string `s`, return the length of the longest *contiguous* substring
in which no character appears more than once. An empty string gives 0.

思路
----
暴力做法：枚举所有子串再检查是否有重复，时间 O(n^3)（或用集合优化到 O(n^2)）。

更好的办法是**滑动窗口**（双指针）：用 [left, right] 表示当前"无重复"的窗口，
right 从左往右扫，每次把 s[right] 放进窗口。
用字典 last 记录"每个字符最后一次出现的下标"：
- 如果 s[right] 之前出现过，且那个位置还在窗口里（last[ch] >= left），
  说明窗口里出现了重复，把 left 直接跳到 last[ch] + 1，把旧的那个字符甩出窗口；
- 更新 last[ch] = right，再用 right - left + 1 更新答案。

关键细节：left 只能往右走，不能往回退。比如 "abba"，扫到最后的 'a' 时，
last['a'] = 0 已经在窗口左边（left = 2），这时不能把 left 拉回 1，
所以要判断 last[ch] >= left（等价于 left = max(left, last[ch] + 1)）。

和 10-28 的"两数之和"相比，同样用字典做 O(1) 查找，但多了一个"窗口"的概念：
两个指针都只向右移动，所以总体仍是线性时间。

复杂度 / Complexity
-------------------
- 时间 Time:  O(n)，right 走一遍，left 只前进不后退
- 空间 Space: O(min(n, k))，k 是字符集大小，字典最多存这么多个字符
"""

from __future__ import annotations


def length_of_longest_substring(s: str) -> int:
    last: dict[str, int] = {}  # char -> last index seen
    left = 0
    best = 0
    for right, ch in enumerate(s):
        if ch in last and last[ch] >= left:
            left = last[ch] + 1  # 跳过重复字符，窗口左边界只前进
        last[ch] = right
        best = max(best, right - left + 1)
    return best


def _brute_force(s: str) -> int:
    """O(n^2) 对照实现，用来交叉验证。"""
    best = 0
    for i in range(len(s)):
        seen: set[str] = set()
        for j in range(i, len(s)):
            if s[j] in seen:
                break
            seen.add(s[j])
            best = max(best, j - i + 1)
    return best


if __name__ == "__main__":
    assert length_of_longest_substring("abcabcbb") == 3  # "abc"
    assert length_of_longest_substring("bbbbb") == 1  # "b"
    assert length_of_longest_substring("pwwkew") == 3  # "wke"，注意 "pwke" 不连续
    assert length_of_longest_substring("") == 0
    assert length_of_longest_substring(" ") == 1  # 空格也是字符
    assert length_of_longest_substring("abba") == 2  # left 不能回退
    assert length_of_longest_substring("dvdf") == 3  # "vdf"
    assert length_of_longest_substring("你好你们好") == 3  # "好你们" / "你们好"

    import random

    random.seed(42)
    for _ in range(500):
        t = "".join(random.choice("abcd") for _ in range(random.randint(0, 12)))
        assert length_of_longest_substring(t) == _brute_force(t), t

    print("All tests passed ✅")
