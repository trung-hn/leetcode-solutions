#
# @lc app=leetcode id=684 lang=python3
#
# [684] Redundant Connection
#

# @lc code=start
# TAGS: DFS, BFS, Union Find, Graph

import collections


class UF:
    def __init__(self, n):
        self.parent = list(range(n))

    def union(self, a, b):
        self.parent[self.find(a)] = self.find(b)

    def find(self, a):
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]


class Solution:
    # Simple DFS solution
    # Time O(N^2). Space: O(N)
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def can_reach(source, dest):
            visited = set()
            q = [source]
            for node in q:
                if node == dest:
                    return True
                visited.add(node)
                for nei in neis[node]:
                    if nei in visited:
                        continue
                    q.append(nei)
            return False

        neis = collections.defaultdict(set)
        for a, b in edges:
            neis[a].add(b)
            neis[b].add(a)

        for a, b in reversed(edges):
            neis[a].remove(b)
            neis[b].remove(a)
            if can_reach(a, b):
                return [a, b]
            neis[a].add(b)
            neis[b].add(a)

        return [0]

    # Union Find Solution
    # 45 ms, 98.21%
    # Time: O(NlogN). Space: O(N)
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(len(edges) + 1))

        def find(a):
            if parent[a] != a:
                parent[a] = find(parent[a])
            return parent[a]

        def union(a, b):
            if find(a) == find(b):
                return False
            parent[find(a)] = find(b)
            return True

        # As soon as an union is not needed, we found the answer.
        for a, b in edges:
            if not union(a, b):
                return [a, b]


# @lc code=end
