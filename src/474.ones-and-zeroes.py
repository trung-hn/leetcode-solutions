#
# @lc app=leetcode id=474 lang=python3
#
# [474] Ones and Zeroes
#

# @lc code=start
# TAGS: Dynamic Programming
# REVIEWME: Dynamic Programming
import collections
from functools import cache
from typing import List


class Solution:
    # 6179 nsm, 12%. Manual Memoization. Time and Space: O(N*M*L)
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        mem = {}

        def dp(i, ones, zeroes):
            if (i, ones, zeroes) in mem:
                return mem[(i, ones, zeroes)]
            if ones < 0 or zeroes < 0:
                return float("-inf")
            if i == len(strs):
                return 0

            # Skip this str
            skip = dp(i + 1, ones, zeroes)

            # One, zero of current str
            one, zero = counters[i]["1"], counters[i]["0"]

            # Take this str
            take = dp(i + 1, ones - one, zeroes - zero) + 1
            mem[(i, ones, zeroes)] = max(take, skip)
            return max(take, skip)

        counters = [collections.Counter(s) for s in strs]
        return dp(0, n, m)

    # 2252 ms, 90.27%. Time and Space: O(N*M*L)
    def findMaxForm2(self, strs: List[str], m: int, n: int) -> int:
        @cache
        def dp(i, ones, zeroes):
            if ones < 0 or zeroes < 0:
                return float("-inf")
            if i == len(strs):
                return 0

            # Skip this str
            skip = dp(i + 1, ones, zeroes)

            # One, zero of current str
            one, zero = counters[i]["1"], counters[i]["0"]

            # Take this str
            take = dp(i + 1, ones - one, zeroes - zero) + 1
            return max(take, skip)

        counters = [collections.Counter(s) for s in strs]
        return dp(0, n, m)

    # 4004 ms, 32.59%. Time: O(N*M*L). Space: O(N*M)
    # Bottom-up DP, Rolling Array.
    def findMaxForm3(sezlf, strs: List[str], m: int, n: int) -> int:
        def count(s):
            return sum(1 for c in s if c == "0"), sum(1 for c in s if c == "1")

        prev = [[0] * (n + 1) for _ in range(m + 1)]
        for z, o in [count(s) for s in strs]:
            cur = []
            for x in range(m + 1):
                row = []
                for y in range(n + 1):
                    if x >= z and y >= o:
                        row.append(max(1 + prev[x - z][y - o], prev[x][y]))
                    else:
                        row.append(prev[x][y])
                cur.append(row)
            prev = cur
        return prev[m][n]

    # Bottom-up DP, Rolling Array.
    # Time: O(N*M*L). Space: O(N*M)
    def findMaxForm4(self, strs: List[str], m: int, n: int) -> int:
        def count(s):
            return sum(1 for c in s if c == "0"), sum(1 for c in s if c == "1")

        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for z, o in [count(s) for s in strs]:
            for x in range(m, -1, -1):
                for y in range(n, -1, -1):
                    if x >= z and y >= o:
                        dp[x][y] = max(1 + dp[x - z][y - o], dp[x][y])

        return dp[m][n]


# @lc code=end
