#
# @lc app=leetcode id=1519 lang=python3
#
# [1519] Number of Nodes in the Sub-Tree With the Same Label
#

# @lc code=start
# TAGS: Hash Table, Tree, Depth-First Search, Breadth-First Search, Counting
from collections import defaultdict, Counter


class Solution:
    # Time and Space: O(N)
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:

        def dfs(node, parent=None):
            counter = Counter(labels[node])
            for nei in neis[node]:
                if nei == parent:
                    continue
                counter += dfs(nei, node)
            ans[node] = counter[labels[node]]
            return counter

        neis = defaultdict(list)
        for a, b in edges:
            neis[a].append(b)
            neis[b].append(a)

        ans = [0] * n
        dfs(0)
        return ans


# @lc code=end
