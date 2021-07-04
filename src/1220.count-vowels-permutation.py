#
# @lc app=leetcode id=1220 lang=python3
#
# [1220] Count Vowels Permutation
#

# @lc code=start
# TAGS: Dynamic Programming


class Solution:
    # 708 ms, 20.26%. Time: O(N). Space: O(N)
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10**9 + 7
        neis = {"": "aeuio", "a": "e", "e": "ai",
                "i": "aeuo", "o": "ui", "u": "a"}

        @cache
        def dfs(cur="", length=0):
            if length == n:
                return 1
            rv = 0
            for nei in neis[cur]:
                rv += dfs(nei, length + 1)
            return rv % MOD
        return dfs() % MOD


# @lc code=end
