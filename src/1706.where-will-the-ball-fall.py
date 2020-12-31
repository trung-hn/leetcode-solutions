#
# @lc app=leetcode id=1706 lang=python3
#
# [1706] Where Will the Ball Fall
#

# @lc code=start
# TAGS: Dynamic Programming
class Solution:
    # 196 ms, 86.30%. Time: O(M*N). Space: O(M)
    def findBall(self, grid: List[List[int]]) -> List[int]:
        def dfs(r, c):
            if r == R: return c
        
            cell = grid[r][c]
            if c > 0 and cell == -1:
                if grid[r][c - 1] == 1: return -1
                return dfs(r + 1, c - 1)
            if c < C - 1 and cell == 1:
                if grid[r][c + 1] == -1: return -1
                return dfs(r + 1, c + 1)
            return -1
        
        R, C = len(grid), len(grid[0])
        ans = []
        for c in range(C):
            ans.append(dfs(0, c))
        return ans
# @lc code=end

