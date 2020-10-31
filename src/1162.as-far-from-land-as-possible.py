#
# @lc app=leetcode id=1162 lang=python3
#
# [1162] As Far from Land as Possible
#

# @lc code=start
# TAGS: Graph, BFS
class Solution:
    # 1064 ms, 13.64% => 616 ms, 59.54%. Time and Space: O(M*N)
    # `if grid[r][c] < 0: continue` reduces time by 2 times
    def maxDistance(self, grid: List[List[int]]) -> int:
        R = len(grid); C = len(grid[0])
        islands = [(r, c) for r in range(R) for c in range(C) if grid[r][c]]
        q = [(r, c, 0) for r, c in islands]
        
        for r, c, depth in q:
            if grid[r][c] < 0: continue
            if grid[r][c] == 0:
                grid[r][c] = depth
                
            for x, y in (r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1):
                if 0 <= x < R and 0 <= y < C and grid[x][y] == 0:
                    q.append((x, y, depth - 1))
            
        # Important lesson: min(grid) does not return min by row, it returns smallest TUPLE
        max_distance = -min(r for row in grid for r in row)
        return max_distance if max_distance > 0 else -1

# @lc code=end

