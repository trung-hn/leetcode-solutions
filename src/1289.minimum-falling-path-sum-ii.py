#
# @lc app=leetcode id=1289 lang=python3
#
# [1289] Minimum Falling Path Sum II
#


# @lc code=start
# TAGS: Array, Dynamic Programming, Matrix
class Solution:
    # Time: O(R*C*C). Space: O(1)
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        for i in range(1, R):
            for j in range(C):
                grid[i][j] += min(
                    [grid[i - 1][k] for k in range(C) if k != j], default=0
                )
        return min(grid[-1])


# @lc code=end
