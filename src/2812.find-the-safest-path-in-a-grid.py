#
# @lc app=leetcode id=2812 lang=python3
#
# [2812] Find the Safest Path in a Grid
#


# @lc code=start
# TAGS: Array, Binary Search, Breadth-First Search, Union Find, Matrix
import heapq


class Solution:
    # Time and Space: O(R*C)
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:

        R, C = len(grid), len(grid[0])
        queue = [(r, c) for r in range(R) for c in range(C) if grid[r][c]]
        dist = 1
        while queue:
            next_queue = set()
            for r, c in queue:
                for nr, nc in (r + 1, c), (r - 1, c), (r, c - 1), (r, c + 1):
                    if 0 <= nr < R and 0 <= nc < C and not grid[nr][nc]:
                        grid[nr][nc] = dist + 1
                        next_queue.add((nr, nc))
            queue = next_queue
            dist += 1

        heap = [(-grid[0][0], 0, 0)]
        visited = set([(0, 0)])
        ans = grid[0][0]
        while heap:
            dist, r, c = heapq.heappop(heap)
            ans = min(ans, -dist)
            if r == R - 1 and c == C - 1:
                return ans - 1
            for nr, nc in (r + 1, c), (r - 1, c), (r, c - 1), (r, c + 1):
                if 0 <= nr < R and 0 <= nc < C and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    heapq.heappush(heap, (-grid[nr][nc], nr, nc))


# @lc code=end
