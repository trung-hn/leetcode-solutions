#
# @lc app=leetcode id=827 lang=python3
#
# [827] Making A Large Island
#

# @lc code=start
# TAGS: Array, DFS, BFS, Union-Find, Matrix


class Solution:
    # Time and Space: O(N^2)
    def largestIsland(self, grid: List[List[int]]) -> int:

        # Id used to assign to islands
        self.island_id = 2

        def dfs(r, c):
            grid[r][c] = self.island_id
            cnt = 1
            for x, y in (r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1):
                if 0 <= x < R and 0 <= y < C and grid[x][y] == 1:
                    cnt += dfs(x, y)
            return cnt

        # Assign id to island and record their sizes
        R, C = len(grid), len(grid[0])
        counter = {}
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    counter[self.island_id] = dfs(r, c)
                    self.island_id += 1

        def make_this_island(r, c):
            neis = set()
            for x, y in (r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1):
                if 0 <= x < R and 0 <= y < C and grid[x][y] != 0:
                    neis.add(grid[x][y])
            return sum(counter[nei] for nei in neis) + 1

        # Go through each water tile and make it a land.
        result = max(counter.values()) if counter else 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    result = max(result, make_this_island(r, c))

        return result
# @lc code=end
