#
# @lc app=leetcode id=861 lang=python3
#
# [861] Score After Flipping Matrix
#


# @lc code=start
# TAGS: Array, Greedy, Bit Manipulation, Matrix
class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        for r in range(R):
            if grid[r][0] == 0:
                for c in range(C):
                    grid[r][c] = 1 - grid[r][c]
        ans = 0
        for c in range(C):
            ones = sum(grid[r][c] == 1 for r in range(R))
            ones = max(ones, R - ones)
            ans += ones * 1 << (C - c - 1)
        return ans


# @lc code=end
