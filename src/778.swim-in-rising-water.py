#
# @lc app=leetcode id=778 lang=python3
#
# [778] Swim in Rising Water
#

# @lc code=start
# TAGS: Binary Search, Heap, DFS, Union Find


class Solution:
    # 9116 ms, 1%. Time: O(R*C*R*C). Space: O(R*C). DP with memoization
    def swimInWater(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        visited = set()
        @cache
        def dfs(r=0, c=0, max_sofar=0):
            if r == R - 1 and c == C - 1:
                return max_sofar

            rv = float("inf")
            for x, y in (r - 1, c), (r + 1, c), (r, c + 1), (r, c - 1):
                if 0 <= x < R and 0 <= y < C and (x, y) not in visited:
                    visited.add((x, y))
                    rv = min(rv, dfs(x, y, max(max_sofar, grid[x][y])))
                    visited.discard((x, y))
            return rv
        return dfs(max_sofar=grid[0][0])

    # 96 ms, 88.49%. Time: O(R*C*logN). Space: O(R*C) From lee215 discussion. Heap
    def swimInWater(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        visited = set()
        heap = [[grid[0][0], 0, 0]]
        result = 0
        while True:
            val, r, c = heapq.heappop(heap)
            result = max(result, val)
            if r == R - 1 and c == C - 1:
                return result

            for x, y in (r - 1, c), (r + 1, c), (r, c + 1), (r, c - 1):
                if 0 <= x < R and 0 <= y < C and (x, y) not in visited:
                    visited.add((x, y))
                    heapq.heappush(heap, (grid[x][y], x, y))


# @lc code=end
