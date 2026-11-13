"""
网络延迟时间 Network Delay Time (Day 16 · 2026-11-12)

题目（自己的话）：
有 n 个网络节点，编号 1..n。times 里每一项 (u, v, w) 表示从 u 发信号到 v
需要 w 的时间（有向边，w >= 0）。现在从节点 k 发出一个信号，问所有节点
都收到信号最少需要多久？如果有节点永远收不到，返回 -1。

思路：
这就是“单源最短路”：答案 = 从 k 到每个节点最短距离中的最大值。
边权非负，所以用 Dijkstra（堆优化）：
1) 建邻接表 graph[u] = [(v, w), ...]。
2) 小根堆里放 (当前距离, 节点)，从 (0, k) 开始。
3) 每次弹出距离最小的节点 u：如果它已经确定过最短距离（在 dist 里），跳过；
   否则 dist[u] = d 就是最终最短距离（贪心正确性来自边权非负：
   之后再绕路只会更长）。然后把 u 的邻居 (d + w, v) 推进堆。
4) 结束后若 dist 的节点数 < n，说明有节点不可达，返回 -1；否则返回 max(dist)。
这里用“懒删除”：同一节点可能在堆里出现多次，弹出时检查是否已确定即可，
省去 decrease-key 操作。

对照解法 Bellman-Ford：把所有边松弛 n-1 轮，O(n·E)，用来随机校验。

复杂度：
- Dijkstra（堆）：时间 O(E log E)，空间 O(n + E)
- Bellman-Ford：时间 O(n·E)，空间 O(n)
"""
import heapq
from collections import defaultdict
from typing import Dict, List, Tuple


def network_delay_time(times: List[Tuple[int, int, int]], n: int, k: int) -> int:
    graph: Dict[int, List[Tuple[int, int]]] = defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))

    dist: Dict[int, int] = {}
    heap = [(0, k)]
    while heap:
        d, u = heapq.heappop(heap)
        if u in dist:  # 懒删除：已经确定过最短距离
            continue
        dist[u] = d
        for v, w in graph[u]:
            if v not in dist:
                heapq.heappush(heap, (d + w, v))

    return max(dist.values()) if len(dist) == n else -1


def network_delay_time_bf(times: List[Tuple[int, int, int]], n: int, k: int) -> int:
    """Bellman-Ford 对照解法。"""
    INF = float("inf")
    dist = [INF] * (n + 1)
    dist[k] = 0
    for _ in range(n - 1):
        for u, v, w in times:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    ans = max(dist[1:])
    return -1 if ans == INF else int(ans)


if __name__ == "__main__":
    import random

    assert network_delay_time([(2, 1, 1), (2, 3, 1), (3, 4, 1)], 4, 2) == 2
    assert network_delay_time([(1, 2, 1)], 2, 1) == 1
    assert network_delay_time([(1, 2, 1)], 2, 2) == -1  # 有向边，2 到不了 1
    assert network_delay_time([], 1, 1) == 0  # 只有自己
    # 直连更贵、绕路更便宜：1->3 直接 10，1->2->3 只要 2
    assert network_delay_time([(1, 3, 10), (1, 2, 1), (2, 3, 1)], 3, 1) == 2
    # 0 权边也没问题
    assert network_delay_time([(1, 2, 0), (2, 3, 0)], 3, 1) == 0
    random.seed(16)
    for _ in range(500):  # 随机对照 Bellman-Ford
        n = random.randint(1, 7)
        times = [
            (random.randint(1, n), random.randint(1, n), random.randint(0, 9))
            for _ in range(random.randint(0, 15))
        ]
        k = random.randint(1, n)
        assert network_delay_time(times, n, k) == network_delay_time_bf(times, n, k), (times, n, k)
    print("all tests passed")
