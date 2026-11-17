"""
滑动窗口最大值 Sliding Window Maximum (Day 20 · 2026-11-16)

题目（自己的话）：
给一个整数数组 nums 和窗口大小 k。一个长度为 k 的窗口从最左边开始，
每次向右滑动一格，直到碰到数组末尾。返回每个窗口位置里的最大值组成的列表。
例如 nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3 → [3, 3, 5, 5, 6, 7]。

思路（单调队列 monotonic deque）：
暴力做法是每个窗口都扫一遍取 max，时间 O(n·k)，k 大时太慢。
关键观察：如果新来的元素 x 比队尾某个旧元素 y 大（或相等），
那么 y 以后再也不可能成为最大值——x 比它大，而且比它更晚离开窗口。
所以可以把 y 直接丢掉。

于是维护一个双端队列 dq，里面存“下标”，满足对应的值从队头到队尾单调递减：
1. 新元素 nums[i] 入队前，把队尾所有 <= nums[i] 的下标弹出（它们没用了）；
2. 把 i 加到队尾；
3. 如果队头下标已经滑出窗口（dq[0] <= i - k），从队头弹出；
4. 当 i >= k - 1 时，窗口已经满了，队头 nums[dq[0]] 就是当前窗口最大值。

为什么存下标而不是值？因为要判断队头是否已经离开窗口，需要知道位置。

对照解法：
- 暴力 O(n·k)，用随机数据交叉校验；
- 大顶堆 + 懒删除 O(n log n)：堆里放 (-值, 下标)，堆顶下标出窗口就弹掉。

复杂度（n = len(nums)）：
- 单调队列：时间 O(n)（每个下标最多入队一次、出队一次），额外空间 O(k)
- 堆：时间 O(n log n)，空间 O(n)
"""
import heapq
import random
from collections import deque
from typing import List


def max_sliding_window(nums: List[int], k: int) -> List[int]:
    if k <= 0 or not nums:
        return []
    k = min(k, len(nums))
    dq: deque = deque()  # 存下标，对应的值从队头到队尾单调递减
    result: List[int] = []
    for i, x in enumerate(nums):
        # 1) 队尾比 x 小或相等的元素永远不会再当最大值，弹掉
        while dq and nums[dq[-1]] <= x:
            dq.pop()
        dq.append(i)
        # 2) 队头滑出窗口就弹掉
        if dq[0] <= i - k:
            dq.popleft()
        # 3) 窗口满了就记录答案
        if i >= k - 1:
            result.append(nums[dq[0]])
    return result


def max_sliding_window_heap(nums: List[int], k: int) -> List[int]:
    if k <= 0 or not nums:
        return []
    k = min(k, len(nums))
    heap: List[tuple] = []
    result: List[int] = []
    for i, x in enumerate(nums):
        heapq.heappush(heap, (-x, i))
        if i >= k - 1:
            while heap[0][1] <= i - k:  # 懒删除：堆顶已出窗口
                heapq.heappop(heap)
            result.append(-heap[0][0])
    return result


def max_sliding_window_brute(nums: List[int], k: int) -> List[int]:
    if k <= 0 or not nums:
        return []
    k = min(k, len(nums))
    return [max(nums[i:i + k]) for i in range(len(nums) - k + 1)]


if __name__ == "__main__":
    # 经典样例
    assert max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
    # k = 1：每个元素自己就是最大值
    assert max_sliding_window([4, -2, 7], 1) == [4, -2, 7]
    # k = 数组长度：只有一个窗口
    assert max_sliding_window([9, 11], 2) == [11]
    # 单调递减 / 单调递增
    assert max_sliding_window([5, 4, 3, 2, 1], 2) == [5, 4, 3, 2]
    assert max_sliding_window([1, 2, 3, 4, 5], 2) == [2, 3, 4, 5]
    # 有重复值
    assert max_sliding_window([2, 2, 2, 1, 2], 3) == [2, 2, 2]
    # 边界：空数组 / k 比数组长
    assert max_sliding_window([], 3) == []
    assert max_sliding_window([1, 5, 2], 10) == [5]
    assert max_sliding_window_heap([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]

    # 随机数据：三种解法交叉校验
    rng = random.Random(20261116)
    for _ in range(500):
        n = rng.randint(1, 30)
        nums = [rng.randint(-10, 10) for _ in range(n)]
        k = rng.randint(1, n)
        expected = max_sliding_window_brute(nums, k)
        assert max_sliding_window(nums, k) == expected, (nums, k)
        assert max_sliding_window_heap(nums, k) == expected, (nums, k)

    print("All tests passed ✅")
