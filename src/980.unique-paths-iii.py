#
# @lc app=leetcode id=980 lang=python3
#
# [980] Unique Paths III
#

# @lc code=start
# TAGS: Backtracking, DFS
class Solution:
    # 56 ms, 82.7 %. Back tracking. Time: O(2^N). Space: O(N). N = R * C
    def uniquePathsIII(self, grid: List[List[int]]) -> int:

        def dfs(xy):
            if xy in visited: return            
            if xy == self.end:
                if len(visited) == self.zeroes + 1:
                    self.ans += 1
                else:
                    return
            
            visited.add(xy)
            x, y = xy
            for r, c in (x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y):
                if 0 <= r < R and 0 <= c < C and grid[r][c] in (0, 2):
                    dfs((r, c))
            visited.remove(xy)
        
        R, C = len(grid), len(grid[0])
        self.zeroes = sum(cell == 0 for row in grid for cell in row)
        visited = set()
        
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    start = (r, c)
                elif grid[r][c] == 2:
                    self.end = (r, c)
                    
        self.ans = 0
        dfs(start)
        return self.ans
# @lc code=end

