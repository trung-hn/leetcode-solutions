#
# @lc app=leetcode id=1905 lang=python3
#
# [1905] Count Sub Islands
#

# @lc code=start
# TAGS: Array, DFS, BFS, Union-Find, Matrix

from typing import List


class Solution:
    # 3100 ms, 80.55%. Time and Space: O(N*M)
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:

        def mark_island(r, c, mark):
            grid2[r][c] = mark
            for x, y in (r, c + 1), (r, c - 1), (r + 1, c), (r - 1, c):
                if 0 <= x < R and 0 <= y < C and grid2[x][y] == 1:
                    mark_island(x, y, mark)

        # Mark island on grid2
        R, C = len(grid2), len(grid2[0])
        mark = -1
        for r in range(R):
            for c in range(C):
                if grid2[r][c] == 1:
                    mark_island(r, c, mark)
                    mark -= 1

        # grid2 -= grid1
        for r in range(R):
            for c in range(C):
                if grid1[r][c]:
                    grid2[r][c] = 0

        # Count
        islands_before = ~mark
        islands_after = len(set(val for row in grid2 for val in row)) - 1
        return islands_before - islands_after
# @lc code=end
