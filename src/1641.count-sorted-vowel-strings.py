#
# @lc app=leetcode id=1641 lang=python3
#
# [1641] Count Sorted Vowel Strings
#

# @lc code=start
# TAGS: Dynamic Programming, Math, Backtracking
class Solution:
    """
    There is a Math solution with O(1) Complexity
    """
    # 32 ms, 69.6%. Time and Space: O(N). DFS with memo
    def countVowelStrings(self, n: int) -> int:
        @lru_cache(None)
        def dfs(start=0, length=0):
            if sofar == n:
                return 1
            rv = 0
            for i in range(start, 5):
                rv += dfs(i, length + 1)
            return rv
        return dfs()
    
    # 24 ms, 96.29%. Time: O(N). Space: O(1). DP
    def countVowelStrings(self, n: int) -> int:
        dp = [1, 1, 1, 1, 1]
        for _ in range(n):
            new_dp = [0, 0, 0, 0, 0]
            curr = 0
            for i in range(5):
                curr += dp[i]
                new_dp[i] = curr
            dp = new_dp
        return dp[-1]

    # 24 ms, 96.29%. Same as above but cleaner
    def countVowelStrings(self, n: int) -> int:
        dp = [0, 1, 1, 1, 1, 1]
        for _ in range(n):
            for i in range(1, 6):
                dp[i] += dp[i - 1]
        return dp[-1]
# @lc code=end

