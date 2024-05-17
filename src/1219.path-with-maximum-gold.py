#
# @lc app=leetcode id=1219 lang=python3
#
# [1219] Path with Maximum Gold
#


# @lc code=start
# TAGS: Backtracking
class Solution:
    # 1248 ms, 73.98%. Time: O(R*C+N*2^N) where N is cell with gold (max=25). Space: O(N)
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs(r, c):
            rv = 0
            gold, grid[r][c] = grid[r][c], 0
            for x, y in (r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1):
                if 0 <= x < R and 0 <= y < C and grid[x][y] and grid[x][y]:
                    rv = max(rv, dfs(x, y))
            grid[r][c] = gold
            return rv + gold

        R, C = len(grid), len(grid[0])
        return max(
            [dfs(r, c) for r in range(R) for c in range(C) if grid[r][c]], default=0
        )


# @lc code=end
