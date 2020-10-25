#
# @lc app=leetcode id=1510 lang=python3
#
# [1510] Stone Game IV
#

# @lc code=start
# TAGS: Dynamic Programming
# REVIEWME: Dynamic Programming
import functools
class Solution:
    # 1496 ms, 61.76%. Time: O(N * N^0.5). Space: O(N)
    def winnerSquareGame(self, n: int) -> bool:
        squares = [i**2 for i in range(1, int(n**0.5) + 1)]
        @functools.lru_cache(maxsize=None)
        def dfs(remain):
            if remain == 0:
                return False
            
            for square in squares:
                if square > remain: break
                # Check if there is anyway to win the next step, if yes, then return True for the current play.
                # Notice that players will alternate one another.
                if not dfs(remain - square):
                    return True
            return False
        return dfs(n)

    # 928 ms, 81.70%. Convert above solution to dp. Time: O(N * N^0.5). Space: O(N)
    def winnerSquareGame(self, n: int) -> bool:
        squares = [i**2 for i in range(1, int(n**0.5) + 1)]
        dp = [False] * (n + 1)
        for i in range(1, n + 1):
            for square in squares:
                if square > i: break
                if dp[i - square] == False:
                    dp[i] = True
                    break
        return dp[n]
            
# @lc code=end

