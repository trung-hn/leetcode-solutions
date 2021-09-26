#
# @lc app=leetcode id=1293 lang=python3
#
# [1293] Shortest Path in a Grid with Obstacles Elimination
#

# @lc code=start
# TAGS: Array, BFS, Matrix


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        R, C = len(grid), len(grid[0])
        self.visited = set([(0, 0, 0)])
        queue = [(0, 0, 0, 0)]
        for r, c, depth, obstacle in queue:
            if obstacle > k:
                continue
            if r == R - 1 and c == C - 1:
                return depth
            for x, y in (r, c + 1), (r, c - 1), (r + 1, c), (r - 1, c):
                if 0 <= x < R and 0 <= y < C:
                    obstacle += grid[x][y]
                    if (x, y, obstacle) not in self.visited:
                        self.visited.add((x, y, obstacle))
                        queue.append((x, y, depth + 1, obstacle))
        return -1
# @lc code=end
