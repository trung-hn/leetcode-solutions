#
# @lc app=leetcode id=463 lang=python3
#
# [463] Island Perimeter
#

# @lc code=start
# TAGS: Greedy
class Solution:
    # 720 ms, pythonic but slow
    def islandPerimeter1(self, grid: List[List[int]]) -> int:
        def no_island(r, c):
            total = sum(1 for dx in (-1, 1) if 0 <= r + dx < R and grid[r+dx][c])
            total += sum(1 for dy in (-1, 1) if 0 <= c + dy < C and grid[r][c+dy])
            return total
        
        R, C = len(grid), len(grid[0])
        return sum(4-no_island(r, c) for r in range(R) for c in range(C) if grid[r][c])
    
    # 512 ms, 99% the area is recalculate each time. This explain the -2
    # Time: O(M*N), Space: O(1)
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]: 
                    ans += 4
                    if r and grid[r-1][c]: 
                        ans -= 2
                    if c and grid[r][c-1]: 
                        ans -= 2
        return ans
# @lc code=end

