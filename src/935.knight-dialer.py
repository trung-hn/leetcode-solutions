#
# @lc app=leetcode id=935 lang=python3
#
# [935] Knight Dialer
#

# @lc code=start
# TAGS: Dynamic Programming
import sys
sys.setrecursionlimit(5010)
class Solution:

    # 2800 ms, 24.18%. Time and Space: O(N). Recursion with memoization
    def knightDialer(self, n: int) -> int:
        future_moves = {1: [6, 8], 2: [7, 7], 0:[4, 4], 3: [4, 8], 4:[0, 9, 3], 6:[0, 1, 7], 7:[2, 6], 8:[1, 1], 9:[2, 4]}
        MOD = 10**9 + 7
        if n == 1: return 10

        #@functools.lru_cache 
        memo = {}
        def dfs(i, depth=1):
            if (i, depth) in memo:
                return memo[(i, depth)]

            if depth == n:
                return 1
            rv = 0
            for move in future_moves[i]:
                rv += dfs(move, depth + 1)
            memo[(i, depth)] = rv
            return rv

        ans = 0 
        for i in range(10):
            if i in (3, 5, 6, 9): continue
            elif i in (1, 4, 7):
                ans += dfs(i)*2
            else:# 2 8
                ans += dfs(i)
        return ans % MOD
    
    # 832 ms, 87.51%. Time: O(N). Space: O(1). DP
    # To get to this, think about the time complexity of memoization:
    # [0, 1] [1, 1] [2, 1] ... [9, 1]
    # [0, 2] [1, 2] [2, 2] ... [9, 2]
    # ...
    # [0, n] [1, n] [2, n] ... [9, n]
    def knightDialer1(self, n: int) -> int:
        future_moves = {1: [6, 8], 2: [7, 7], 0:[4, 4], 3: [4, 8], 4:[0, 9, 3], 6:[0, 1, 7], 7:[2, 6], 8:[1, 1], 9:[2, 4]}
        MOD = 10**9 + 7
        dp = [1]*10
        for _ in range(1, n):
            new_dp = [0]*10
            for i in [0, 1, 2, 3, 4, 6, 7, 8, 9]:
                for move in future_moves[i]:
                    new_dp[i] += dp[move]
                new_dp[i] %= MOD
            dp = new_dp
        return sum(dp) % MOD
# @lc code=end

