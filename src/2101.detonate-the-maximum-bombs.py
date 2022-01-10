#
# @lc app=leetcode id=2101 lang=python3
#
# [2101] Detonate the Maximum Bombs
#

# @lc code=start
# TAGS: Array, Math, DFS, BFS, Graph, Geometry

from typing import List
import collections


class Solution:
    # 965 ms, 54.55%. Time and Space: O(E*V)
    def maximumDetonation(self, bombs: List[List[int]]) -> int:

        # Create graph
        neis = collections.defaultdict(list)
        for i1, (x1, y1, r1) in enumerate(bombs):
            for i2, (x2, y2, r2) in enumerate(bombs):
                if i1 == i2:
                    continue
                dist = (y2 - y1) ** 2 + (x2 - x1) ** 2
                if dist <= r1 ** 2:
                    neis[i1].append(i2)

        # Detonate the current bomb
        def dfs(i):
            visited[i] = 1
            for nei in neis[i]:
                if visited[nei]:
                    continue
                dfs(nei)

        # Detonate every bomb and check each of them
        ans = 0
        for bomb in range(len(bombs)):
            visited = [0] * len(bombs)
            dfs(bomb)
            ans = max(ans, sum(visited))
        return ans

# @lc code=end
