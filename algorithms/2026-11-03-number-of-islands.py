"""
Day 7 (2026-11-03) 岛屿数量 Number of Islands

题目（自述）：给定一个由 '1'（陆地）和 '0'（水）组成的二维网格，
上下左右相连的陆地组成一座岛屿，求岛屿的数量。

思路：
逐格扫描，遇到一个未访问的 '1' 就说明发现了一座新岛，计数 +1，
然后用 BFS（队列）把与它相连的所有陆地标记为已访问（这里直接改成 '0'），
这样同一座岛不会被重复计数。用 BFS 而不用递归 DFS，可以避免大网格时递归过深。

复杂度：时间 O(m*n)，每个格子最多入队一次；空间 O(min(m, n)) ~ O(m*n)（队列）。
"""
from collections import deque
from typing import List


def num_islands(grid: List[List[str]]) -> int:
    if not grid:
        return 0
    g = [row[:] for row in grid]  # 拷贝，避免修改调用者的数据
    m, n = len(g), len(g[0])
    count = 0
    for i in range(m):
        for j in range(n):
            if g[i][j] != "1":
                continue
            count += 1
            g[i][j] = "0"
            q = deque([(i, j)])
            while q:
                r, c = q.popleft()
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and g[nr][nc] == "1":
                        g[nr][nc] = "0"
                        q.append((nr, nc))
    return count


if __name__ == "__main__":
    assert num_islands([list("11110"), list("11010"), list("11000"), list("00000")]) == 1
    assert num_islands([list("11000"), list("11000"), list("00100"), list("00011")]) == 3
    assert num_islands([list("000")]) == 0
    assert num_islands([list("101"), list("010"), list("101")]) == 5
    assert num_islands([]) == 0
    print("all tests passed")
