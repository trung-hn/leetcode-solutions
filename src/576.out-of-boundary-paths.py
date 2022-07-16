#
# @lc app=leetcode id=576 lang=python3
#
# [576] Out of Boundary Paths
#
# TAGS: Dynamic Programming
import functools

# @lc code=start
class Solution:
    # 146 ms, 77.75%. Time and Space: O(N*m*n)
    def findPaths(
        self, m: int, n: int, maxMove: int, startRow: int, startColumn: int
    ) -> int:
        M = 10 ** 9 + 7

        @functools.cache
        def dfs(r, c, N):
            if N <= 0:
                return 0
            total = 0
            for x, y in (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1):
                if 0 <= x < R and 0 <= y < C:
                    total += dfs(x, y, N - 1)
            return (total + (0, R - 1).count(r) + (0, C - 1).count(c)) % M

        R, C = m, n
        return dfs(startRow, startColumn, maxMove)


# @lc code=end
