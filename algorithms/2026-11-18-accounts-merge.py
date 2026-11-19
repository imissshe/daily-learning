"""
账户合并 Accounts Merge (Day 22 · 2026-11-18)

题目（自己的话）：
给一组账户 accounts，每个账户是一个列表：第一个元素是用户名，后面是若干邮箱。
只要两个账户有任意一个相同的邮箱，它们就属于同一个人（关系可以传递：
A 和 B 共享邮箱、B 和 C 共享邮箱，则 A、B、C 是同一个人）。
注意：名字相同不代表是同一个人，只有共享邮箱才算。
请合并属于同一个人的账户，输出每个人：[名字, 排好序的去重邮箱...]。

思路（并查集 Union-Find / Disjoint Set Union）：
把每个邮箱看成图里的一个节点。同一个账户里的邮箱彼此连通——
只需要把账户里的每个邮箱都和该账户的第一个邮箱 union 一下即可（星形连接，
不用两两相连）。所有账户处理完后，同一个连通分量里的邮箱就属于同一个人。

并查集两个经典优化：
1. 路径压缩 path compression：find 时把沿途节点直接挂到根上，下次查询更快；
2. 按秩合并 union by rank/size：总是把小树挂到大树下面，避免树退化成链。
两者合用后，单次操作的均摊复杂度是 O(α(n))，α 是反阿克曼函数，实际可视为常数。

最后按根分组：root -> [邮箱...]，每组排序，再加上名字（用 email_to_name 记录）。

对照解法：DFS 建图求连通分量，用随机数据交叉校验两种实现结果一致。

复杂度（N = 邮箱总数，含重复出现）：
- 时间 O(N·α(N)) 做合并 + O(N log N) 排序输出
- 空间 O(N)
"""
import random
from collections import defaultdict
from typing import Dict, List


class DSU:
    """并查集：路径压缩 + 按大小合并。"""

    def __init__(self) -> None:
        self.parent: Dict[str, str] = {}
        self.size: Dict[str, int] = {}

    def add(self, x: str) -> None:
        if x not in self.parent:
            self.parent[x] = x
            self.size[x] = 1

    def find(self, x: str) -> str:
        # 迭代版路径压缩：先找到根，再把沿途节点都直接指向根
        root = x
        while self.parent[root] != root:
            root = self.parent[root]
        while self.parent[x] != root:
            self.parent[x], x = root, self.parent[x]
        return root

    def union(self, a: str, b: str) -> bool:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra  # 小树挂到大树下
        self.size[ra] += self.size[rb]
        return True


def accounts_merge(accounts: List[List[str]]) -> List[List[str]]:
    dsu = DSU()
    email_to_name: Dict[str, str] = {}
    for account in accounts:
        name, emails = account[0], account[1:]
        for email in emails:
            dsu.add(email)
            email_to_name[email] = name
            dsu.union(emails[0], email)  # 和本账户第一个邮箱连起来

    groups: Dict[str, List[str]] = defaultdict(list)
    for email in dsu.parent:
        groups[dsu.find(email)].append(email)

    result = [[email_to_name[root]] + sorted(emails) for root, emails in groups.items()]
    result.sort()  # 输出顺序题目不要求，排序后方便测试比较
    return result


def accounts_merge_dfs(accounts: List[List[str]]) -> List[List[str]]:
    """对照解法：邮箱建无向图，DFS 求连通分量。"""
    graph: Dict[str, set] = defaultdict(set)
    email_to_name: Dict[str, str] = {}
    for account in accounts:
        name, emails = account[0], account[1:]
        for email in emails:
            graph[email].add(emails[0])
            graph[emails[0]].add(email)
            email_to_name[email] = name

    seen: set = set()
    result: List[List[str]] = []
    for start in graph:
        if start in seen:
            continue
        seen.add(start)
        stack, component = [start], []
        while stack:  # 用显式栈，避免递归过深
            node = stack.pop()
            component.append(node)
            for nxt in graph[node]:
                if nxt not in seen:
                    seen.add(nxt)
                    stack.append(nxt)
        result.append([email_to_name[start]] + sorted(component))
    result.sort()
    return result


if __name__ == "__main__":
    # 1) 经典样例：前两个 John 共享 johnsmith@mail.com，合并；第三个 John 是另一个人
    accounts = [
        ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
        ["John", "johnsmith@mail.com", "john00@mail.com"],
        ["Mary", "mary@mail.com"],
        ["John", "johnnybravo@mail.com"],
    ]
    expected = [
        ["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"],
        ["John", "johnnybravo@mail.com"],
        ["Mary", "mary@mail.com"],
    ]
    assert accounts_merge(accounts) == expected
    assert accounts_merge_dfs(accounts) == expected

    # 2) 传递性：A-B 共享 b，B-C 共享 c，三者合并成一人
    chain = [["Ann", "a", "b"], ["Ann", "b", "c"], ["Ann", "c", "d"]]
    assert accounts_merge(chain) == [["Ann", "a", "b", "c", "d"]]

    # 3) 同一账户内重复邮箱要去重；单邮箱账户原样输出
    assert accounts_merge([["Bob", "x", "x", "y"]]) == [["Bob", "x", "y"]]
    assert accounts_merge([["Eve", "e"]]) == [["Eve", "e"]]
    assert accounts_merge([]) == []

    # 4) 并查集本身：union 返回是否真正合并，find 路径压缩后直接指向根
    d = DSU()
    for ch in "abcd":
        d.add(ch)
    assert d.union("a", "b") and d.union("c", "d") and d.union("b", "d")
    assert not d.union("a", "c")  # 已在同一集合
    assert len({d.find(ch) for ch in "abcd"}) == 1

    # 5) 随机数据：并查集与 DFS 结果一致
    rng = random.Random(2026)
    for _ in range(300):
        pool = [f"u{i}@mail.com" for i in range(rng.randint(1, 15))]
        accs = []
        for _ in range(rng.randint(0, 8)):
            emails = rng.sample(pool, rng.randint(1, min(4, len(pool))))
            accs.append(["P"] + emails)
        assert accounts_merge(accs) == accounts_merge_dfs(accs)

    print("all tests passed ✅")
