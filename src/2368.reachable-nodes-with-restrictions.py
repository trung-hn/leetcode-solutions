#
# @lc app=leetcode id=2368 lang=python3
#
# [2368] Reachable Nodes With Restrictions
#

# @lc code=start
# TAGS: Array, Hash Table, Tree, BFS, DFS, Graph
from collections import defaultdict


class Solution:
    # 1258 ms, 90.52%
    # Time and Space: O(V + E)
    def reachableNodes(
        self, n: int, edges: List[List[int]], restricted: List[int]
    ) -> int:
        neis = defaultdict(list)
        for a, b in edges:
            neis[a].append(b)
            neis[b].append(a)

        restricted = set(restricted)

        def dfs(i, parent=None):
            if i in restricted:
                return 0
            total = 1
            for nei in neis[i]:
                if nei == parent:
                    continue
                total += dfs(nei, i)
            return total

        return dfs(0)


# @lc code=end
