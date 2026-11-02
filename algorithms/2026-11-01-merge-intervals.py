"""
2026-11-01 · 合并区间 / Merge Intervals

题目（自己的话）
----------------
给一组闭区间 intervals，每个区间是 [start, end]（start <= end），顺序是乱的。
把所有有重叠的区间合并成一个，返回合并后互不重叠的区间列表（按起点从小到大）。
两个区间只要"碰到"就算重叠，比如 [1, 4] 和 [4, 5] 要合并成 [1, 5]。

Problem (in my own words)
-------------------------
Given an unordered list of closed intervals `[start, end]`, merge every group
of overlapping intervals and return the resulting non-overlapping intervals,
sorted by start. Touching intervals such as [1, 4] and [4, 5] count as
overlapping and become [1, 5].

思路
----
暴力做法：反复两两比较、能合并就合并，直到没有变化，最坏 O(n^2) 甚至更多。

关键观察：**先按起点排序**。排序之后，能和某个区间重叠的区间一定紧挨在它后面，
于是只要从左往右扫一遍，维护"当前正在合并的区间" merged[-1]：
- 如果新区间的起点 start <= merged[-1] 的终点，说明重叠，
  把终点扩展为 max(merged[-1].end, end)；
- 否则说明中间断开了，把新区间作为一个新的段放进结果。

关键细节：
1. 扩展终点时要取 max，不能直接用新区间的 end。
   例如 [1, 10] 和 [2, 3]，合并后仍是 [1, 10]，新区间被"包含"了。
2. 判断条件是 <=（不是 <），因为题目里相接的区间也算重叠。
3. 不要修改调用者传进来的列表：先复制一份再排序，结果里也放新的列表。

和前几天相比：10-28 两数之和用哈希表、10-30 用滑动窗口，
今天的套路是"**排序 + 贪心扫描**"——很多区间类问题（会议室、插入区间、
最少箭射气球）都是先排序，再一遍扫描。

复杂度 / Complexity
-------------------
- 时间 Time:  O(n log n)，瓶颈在排序；扫描本身是 O(n)
- 空间 Space: O(n)，用于排序副本和结果（不计输出的话是排序所需的额外空间）
"""

from __future__ import annotations


def merge(intervals: list[list[int]]) -> list[list[int]]:
    merged: list[list[int]] = []
    for start, end in sorted(intervals, key=lambda iv: iv[0]):
        if merged and start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)  # 重叠：扩展终点，取 max
        else:
            merged.append([start, end])  # 断开：开启新的一段
    return merged


def _brute_force(intervals: list[list[int]]) -> list[list[int]]:
    """对照实现：把每个区间覆盖的点标出来（区间端点都是小整数时可用）。

    用 2*x 表示点 x、2*x+1 表示 x 和 x+1 之间的缝隙，
    这样 [1, 2] 和 [3, 4] 中间的缝隙不会被覆盖，能正确区分"相接"和"断开"。
    """
    covered: set[int] = set()
    for start, end in intervals:
        covered.update(range(2 * start, 2 * end + 1))
    result: list[list[int]] = []
    for p in sorted(covered):
        if result and p == 2 * result[-1][1] + 1:
            continue  # 缝隙，属于当前段
        if result and p == 2 * result[-1][1] + 2 and (p - 1) in covered:
            result[-1][1] = p // 2
        elif p % 2 == 0:
            result.append([p // 2, p // 2])
    return result


if __name__ == "__main__":
    assert merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert merge([[1, 4], [4, 5]]) == [[1, 5]]  # 相接也算重叠
    assert merge([[1, 10], [2, 3]]) == [[1, 10]]  # 被包含，终点要取 max
    assert merge([[8, 10], [1, 3], [2, 6]]) == [[1, 6], [8, 10]]  # 乱序输入
    assert merge([[1, 2], [3, 4]]) == [[1, 2], [3, 4]]  # 不相接，不合并
    assert merge([[5, 5]]) == [[5, 5]]  # 单点区间
    assert merge([]) == []

    original = [[2, 6], [1, 3]]
    merge(original)
    assert original == [[2, 6], [1, 3]]  # 不修改调用者的列表

    import random

    random.seed(42)
    for _ in range(500):
        ivs = []
        for _ in range(random.randint(0, 8)):
            a = random.randint(0, 15)
            ivs.append([a, a + random.randint(0, 5)])
        assert merge(ivs) == _brute_force(ivs), ivs

    print("All tests passed ✅")
