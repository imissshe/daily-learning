"""
Day 11 (2026-11-07) 课程表 Course Schedule

题目（自述）：一共有 num_courses 门课，编号 0..num_courses-1。
prerequisites 里每一项 [a, b] 表示「想修 a，必须先修完 b」。
判断能否修完全部课程；如果能，再给出一种可行的修课顺序（不能则返回空列表）。

思路：
把课程看成有向图的节点，[a, b] 就是一条边 b -> a。
能修完所有课 <=> 这张图里没有环（有环就互相等待，永远修不了）。
用 Kahn 拓扑排序（BFS）：
  1. 统计每门课的入度（还有几门先修课没修）。
  2. 入度为 0 的课可以直接修，先全部放进队列。
  3. 每次从队列取出一门课加入结果，把它指向的后续课入度减 1，
     减到 0 就说明先修课都满足了，入队。
  4. 最后结果里的课程数 == num_courses 则无环、可完成；否则剩下的课都卡在环里。
相比 DFS 三色标记，Kahn 算法顺手就能产出修课顺序，也不用担心递归深度。

复杂度：时间 O(V + E)，V 为课程数、E 为先修关系数；空间 O(V + E)（邻接表 + 入度数组 + 队列）。
"""
from collections import deque
from typing import List


def find_order(num_courses: int, prerequisites: List[List[int]]) -> List[int]:
    graph: List[List[int]] = [[] for _ in range(num_courses)]
    indegree = [0] * num_courses
    for course, pre in prerequisites:
        graph[pre].append(course)
        indegree[course] += 1

    queue = deque(i for i in range(num_courses) if indegree[i] == 0)
    order: List[int] = []
    while queue:
        cur = queue.popleft()
        order.append(cur)
        for nxt in graph[cur]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                queue.append(nxt)

    return order if len(order) == num_courses else []


def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool:
    return len(find_order(num_courses, prerequisites)) == num_courses


def _is_valid_order(num_courses: int, prerequisites: List[List[int]], order: List[int]) -> bool:
    if sorted(order) != list(range(num_courses)):
        return False
    pos = {c: i for i, c in enumerate(order)}
    return all(pos[pre] < pos[course] for course, pre in prerequisites)


if __name__ == "__main__":
    assert can_finish(2, [[1, 0]]) is True
    assert can_finish(2, [[1, 0], [0, 1]]) is False          # 两门课互为先修，成环
    assert can_finish(1, []) is True
    assert can_finish(3, []) is True                          # 没有依赖，随便修
    assert can_finish(3, [[0, 0]]) is False                   # 自环
    assert can_finish(4, [[1, 0], [2, 1], [3, 2], [1, 3]]) is False  # 1->2->3->1 成环

    prereq = [[1, 0], [2, 0], [3, 1], [3, 2]]
    order = find_order(4, prereq)
    assert _is_valid_order(4, prereq, order)                  # 例如 [0, 1, 2, 3]
    assert find_order(2, [[1, 0], [0, 1]]) == []

    prereq = [[5, 4], [4, 3], [3, 2], [2, 1], [1, 0]]
    assert find_order(6, prereq) == [0, 1, 2, 3, 4, 5]        # 一条链只有唯一顺序
    print("all tests passed")
