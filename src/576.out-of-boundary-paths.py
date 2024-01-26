#
# @lc app=leetcode id=576 lang=python3
#
# [576] Out of Boundary Paths
#
# TAGS: Dynamic Programming
# REVIEWME: Dynamic Programming
import functools, collections


# @lc code=start
class Solution:
    # Memoization
    # Time and Space: O(R * C * N)
    def findPaths(
        self, m: int, n: int, maxMove: int, startRow: int, startColumn: int
    ) -> int:
        M = 10**9 + 7

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

    # Optimized for Space Complexity
    # Space: O(R * C * N). Space: O(R * C)
    def findPaths(
        self, m: int, n: int, maxMove: int, startRow: int, startColumn: int
    ) -> int:
        MOD = 10**9 + 7
        dp = collections.defaultdict(int)
        dp[(startRow, startColumn)] = 1
        ans = 0
        R, C = m, n
        for n in range(maxMove):
            temp = collections.defaultdict(int)
            for r in range(R):
                for c in range(C):
                    for x, y in (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1):
                        if 0 <= x < R and 0 <= y < C:
                            # record how many times to get here for this n
                            temp[(x, y)] += dp[(r, c)] % MOD
                        else:
                            # out of bound
                            ans += dp[(r, c)] % MOD
            dp = temp
        return ans % MOD


# @lc code=end
