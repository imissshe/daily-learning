"""
最长递增子序列 Longest Increasing Subsequence (Day 14 · 2026-11-10)

题目（自己的话）：
给一个整数数组 nums，找出其中最长的“严格递增子序列”的长度。
子序列不要求连续，但要保持原来的先后顺序。例如 [10,9,2,5,3,7,101,18]
里的 [2,3,7,18] 长度为 4，就是答案。

思路：
1) 朴素 DP（O(n^2)）：dp[i] 表示以 nums[i] 结尾的 LIS 长度，
   dp[i] = 1 + max(dp[j])，其中 j < i 且 nums[j] < nums[i]。用作对照。
2) 贪心 + 二分（O(n log n)，主解法）：维护数组 tails，
   tails[k] = 所有长度为 k+1 的递增子序列中，“最小的结尾值”。
   结尾越小，后面越容易接上新数字。tails 本身一定严格递增，所以可以二分：
   - 对每个 x，用 bisect_left 找到第一个 >= x 的位置 i；
   - i == len(tails) 说明 x 比所有结尾都大，可以把最长序列延长一位，append；
   - 否则用 x 替换 tails[i]，让长度为 i+1 的序列结尾更小。
   最终 len(tails) 就是答案。注意 tails 不一定是真实的子序列，只有长度是对的。
   用 bisect_left（而非 bisect_right）保证“严格”递增：相等的数会替换而不是延长。

复杂度：
- 贪心 + 二分：时间 O(n log n)，空间 O(n)
- 朴素 DP：时间 O(n^2)，空间 O(n)
"""
from bisect import bisect_left
from typing import List


def length_of_lis(nums: List[int]) -> int:
    tails: List[int] = []
    for x in nums:
        i = bisect_left(tails, x)
        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x
    return len(tails)


def length_of_lis_dp(nums: List[int]) -> int:
    """O(n^2) 对照解法。"""
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp, default=0)


if __name__ == "__main__":
    import random

    assert length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert length_of_lis([0, 1, 0, 3, 2, 3]) == 4
    assert length_of_lis([7, 7, 7, 7]) == 1  # 严格递增，相等不算
    assert length_of_lis([]) == 0
    assert length_of_lis([5]) == 1
    assert length_of_lis([5, 4, 3, 2, 1]) == 1
    assert length_of_lis([1, 2, 3, 4, 5]) == 5
    random.seed(14)
    for _ in range(500):  # 随机对照 O(n^2) 解法
        arr = [random.randint(-5, 5) for _ in range(random.randint(0, 12))]
        assert length_of_lis(arr) == length_of_lis_dp(arr), arr
    print("all tests passed")
