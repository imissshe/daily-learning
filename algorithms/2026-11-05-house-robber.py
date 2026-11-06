"""
Day 9 (2026-11-05) 打家劫舍 House Robber

题目（自述）：一排房子，第 i 家有 nums[i] 现金。相邻两家不能同时偷（会触发警报）。
求在不触发警报的前提下能偷到的最大金额。房子数量可为 0。

思路：
典型一维 DP。令 dp[i] 表示考虑前 i 家（下标 0..i-1）时的最大收益。
对第 i 家只有两种选择：
  - 不偷它：收益 = dp[i-1]
  - 偷它：收益 = dp[i-2] + nums[i-1]
取较大者：dp[i] = max(dp[i-1], dp[i-2] + nums[i-1])。
滚动变量只保留前两态即可，空间降到 O(1)。

复杂度：时间 O(n)；空间 O(1)。
"""
from typing import List


def rob(nums: List[int]) -> int:
    prev2, prev1 = 0, 0  # dp[i-2], dp[i-1]
    for x in nums:
        prev2, prev1 = prev1, max(prev1, prev2 + x)
    return prev1


if __name__ == "__main__":
    assert rob([1, 2, 3, 1]) == 4          # 1 + 3
    assert rob([2, 7, 9, 3, 1]) == 12      # 2 + 9 + 1
    assert rob([]) == 0
    assert rob([5]) == 5
    assert rob([2, 1]) == 2
    assert rob([1, 2]) == 2
    assert rob([10, 1, 1, 10]) == 20       # 两端
    assert rob([0, 0, 0]) == 0
    print("all tests passed")
