"""
2026-10-28 · 两数之和 / Two Sum

题目（自己的话）
----------------
给一个整数列表 nums 和一个目标值 target，找出列表里两个**不同位置**的数，
使它们的和恰好等于 target，返回这两个位置的下标（小的在前）。
可以假设恰好存在一组答案；同一个位置的数不能用两次。

Problem (in my own words)
-------------------------
Given a list of integers `nums` and an integer `target`, find two *different*
positions whose values add up to `target` and return their indices (smaller
first). Exactly one answer exists; an element cannot be paired with itself.

思路
----
暴力做法是两层循环枚举所有数对，时间 O(n^2)。

更好的办法是"边走边查"：从左到右遍历，对当前数 x，需要的另一半是 target - x。
用一个字典 seen 记录"已经见过的数 -> 它的下标"。
- 如果 target - x 已经在 seen 里，说明之前出现过能配对的数，直接返回两个下标；
- 否则把 x 和它的下标存进 seen，继续往后走。

因为是先查再存，所以不会把同一个元素和自己配对；遇到重复值（如 [3, 3]，target=6）
也能正确处理：第二个 3 查到了第一个 3。

复杂度 / Complexity
-------------------
- 时间 Time:  O(n)，每个元素只访问一次，字典查找平均 O(1)
- 空间 Space: O(n)，最坏情况下字典存下所有元素
"""

from __future__ import annotations


def two_sum(nums: list[int], target: int) -> list[int]:
    seen: dict[int, int] = {}  # value -> index
    for i, x in enumerate(nums):
        need = target - x
        if need in seen:
            return [seen[need], i]
        seen[x] = i
    raise ValueError("no pair adds up to target")


def two_sum_brute_force(nums: list[int], target: int) -> list[int]:
    """O(n^2) 对照解法，用来交叉验证 / reference solution for cross-checking."""
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    raise ValueError("no pair adds up to target")


if __name__ == "__main__":
    cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),          # 重复值 duplicates
        ([-4, 1, 9, 5], 1, [0, 3]),   # 负数 negatives
        ([0, 5, 0], 0, [0, 2]),       # 零 zeros
        ([1, 2], 3, [0, 1]),          # 最短输入 minimal input
    ]
    for nums, target, expected in cases:
        assert two_sum(nums, target) == expected, (nums, target)
        assert two_sum_brute_force(nums, target) == expected, (nums, target)

    # 随机交叉验证 / randomized cross-check against brute force
    import random

    rng = random.Random(20261028)
    for _ in range(500):
        nums = rng.sample(range(-1000, 1000), rng.randint(2, 30))
        i, j = sorted(rng.sample(range(len(nums)), 2))
        target = nums[i] + nums[j]
        a, b = two_sum(nums, target)
        assert a < b and nums[a] + nums[b] == target
        c, d = two_sum_brute_force(nums, target)
        assert c < d and nums[c] + nums[d] == target

    try:
        two_sum([1, 2, 3], 100)
        raise AssertionError("expected ValueError")
    except ValueError:
        pass

    print("✅ all tests passed")
