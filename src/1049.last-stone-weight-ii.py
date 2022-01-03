#
# @lc app=leetcode id=1049 lang=python3
#
# [1049] Last Stone Weight II
#

# @lc code=start
# TAGS: Array, Dynamic Programming
# REVIEWME: Dynamic Programming
from functools import cache
from typing import List


class Solution:
    """
    Realization:
    Same as creating 2 subset of numbers such that the difference of their sums is minimal
    For example: 1, 9, 10 will be splitted to (1, 9) and (10)
    Sum of 2 grps = 10 and when we smash stones together, the final answer is minimal. 
    Notice that the smaller stone decide where the left over stone goes to

    Thus, it turns back to classic knapbacks problem because a stone can only be in either set1 or set2. 
    Similar to 494
    """
    # 88 ms, 40.42% Recursive with memoization. Time and Space: O(N * S * S)

    def lastStoneWeightII(self, stones: List[int]) -> int:
        @cache
        def dfs(i=0, S1=0, S2=0):
            if i == len(stones):
                return abs(S1 - S2)
            stone = stones[i]
            return min(dfs(i + 1, S1 + stone, S2), dfs(i + 1, S1, S2 + stone))
        return dfs()

    # 102 ms, 27.23% Time and Space: O(N * S)
    def lastStoneWeightII(self, stones: List[int]) -> int:
        s = sum(stones)
        N = len(stones)
        dp = [[0] * (s + 1) for _ in range(N + 1)]
        dp[0][0] = 1
        for j in range(s + 1):
            for i in range(1, len(dp)):
                stone = stones[i - 1]
                if dp[i - 1][j]:
                    dp[i][j + stone] = 1
                    dp[i][j] = 1

        # Go through all posible sums at dp[-1] and calculate min(abs(diff))
        ans = float("inf")
        for i in range(len(dp[-1])):
            if dp[-1][i]:
                ans = min(ans, abs(s - 2 * i))
        return ans

    # Similar to above but shorter.
    # 54 ms, 72.65% Time and Space: O(N * S)
    def lastStoneWeightII(self, stones: List[int]) -> int:
        """
        Notice that dp will grow as follows:
        {0}
        {0, 1} - prev + 1
        {0, 1, 5, 6} - prev + 5
        {0, 1, 5, 6, 7, 11, 12} - prev + 6
        """
        dp = {0}
        for stone in stones:
            dp |= {stone + val for val in dp}
        s = sum(stones)
        return min(abs(s - 2 * val) for val in dp)


# @lc code=end
