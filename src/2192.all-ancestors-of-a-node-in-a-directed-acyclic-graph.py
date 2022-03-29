#
# @lc app=leetcode id=2192 lang=python3
#
# [2192] All Ancestors of a Node in a Directed Acyclic Graph
#

# @lc code=start
# TAGS: DFS, BFS, Topological Sort, Graph
from typing import List
import collections


class Solution:
    # 800 mns, 90%. Time and Space: O(U+V)
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        memoization = {}

        def dfs(node):
            if node in memoization:
                return memoization[node]

            ancestor = {node}
            for nei in neis[node]:
                ancestor |= dfs(nei)
            memoization[node] = ancestor
            return ancestor

        neis = collections.defaultdict(list)
        for u, v in edges:
            neis[v].append(u)

        ans = [dfs(node) - {node} for node in range(n)]
        return [sorted(grp) for grp in ans]

        # 1527 ms, 25.37%. Time and Space: O(N^2)
    def getAncestors2(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        def dfs(node, root):
            for nei in neis[node]:
                if ans[nei] and ans[nei][-1] == root:
                    continue
                ans[nei].append(root)
                dfs(nei, root)

        neis = collections.defaultdict(list)
        for u, v in edges:
            neis[u].append(v)

        ans = [[] for _ in range(n)]
        for node in range(n):
            dfs(node, node)
        return ans
# @lc code=end
