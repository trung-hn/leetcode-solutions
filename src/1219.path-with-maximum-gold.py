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
        def dfs(r, c, visited=set()):
            rv = 0
            visited.add((r, c))
            for x, y in (r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1):
                if 0 <= x < R and 0 <= y < C and grid[x][y] and (x, y) not in visited:
                    rv = max(rv, dfs(x, y, visited))
            visited.discard((r, c))
            return rv + grid[r][c]
        
        R, C = len(grid), len(grid[0])
        cells_with_gold = [(r, c) for r in range(R) for c in range(C) if grid[r][c]]
        return max(dfs(r, c) for r, c in cells_with_gold) if cells_with_gold else 0
                
# @lc code=end

