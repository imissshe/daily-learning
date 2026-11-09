"""
搜索旋转排序数组 Search in Rotated Sorted Array (Day 12 · 2026-11-08)

题目（自己的话）：
一个元素互不相同的升序数组，被从某个位置“旋转”过（例如 [0,1,2,4,5,6,7] 变成 [4,5,6,7,0,1,2]）。
给定旋转后的数组和目标值 target，返回它的下标，找不到返回 -1。要求时间复杂度 O(log n)。

思路：
二分查找。每次取 mid，左半 [lo, mid] 和右半 [mid, hi] 中至少有一半是有序的。
- 若 nums[lo] <= nums[mid]，左半有序：如果 target 落在 [nums[lo], nums[mid]) 就去左半，否则去右半。
- 否则右半有序：如果 target 落在 (nums[mid], nums[hi]] 就去右半，否则去左半。
每轮都能排除一半，所以是对数级。

复杂度：时间 O(log n)，空间 O(1)。
"""
from typing import List


def search(nums: List[int], target: int) -> int:
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[lo] <= nums[mid]:  # 左半有序
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:  # 右半有序
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1


if __name__ == "__main__":
    assert search([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert search([4, 5, 6, 7, 0, 1, 2], 3) == -1
    assert search([1], 0) == -1
    assert search([1], 1) == 0
    assert search([3, 1], 1) == 1
    assert search([1, 2, 3, 4, 5], 5) == 4  # 未旋转
    assert search([], 1) == -1
    for k in range(8):  # 暴力对照
        arr = list(range(8))
        arr = arr[k:] + arr[:k]
        for t in range(-1, 9):
            assert search(arr, t) == (arr.index(t) if t in arr else -1)
    print("all tests passed")
