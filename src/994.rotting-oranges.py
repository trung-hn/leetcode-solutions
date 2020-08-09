#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#

# @lc code=start
# TAGS: BFS
class Solution:
    # 40 ms, 98%. Time: O(N^2). Space: O(N)
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        # Get location of all rotten oranges
        q = [(r, c, 0) for r in range(R) for c in range(C) if grid[r][c] == 2]
        
        # BFS
        total_time = 0
        for r, c, time in q:
            if grid[r][c] != 0:
                grid[r][c] = 0
                total_time = max(total_time, time)    
                # Added 4 directions
                for x, y in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                    if 0 <= x < R and 0 <= y < C and grid[x][y] == 1:
                        q.append((x, y, time+1))
        
        # return -1 if there is 1 in the grid, else, total_time
        return -1 if any(v==1 for row in grid for v in row) else total_time
# @lc code=end

