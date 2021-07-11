#
# @lc app=leetcode id=639 lang=python3
#
# [639] Decode Ways II
#

# @lc code=start
# TAGS: String, Dynamic Programming


class Solution:
    def numDecodings(self, s: str) -> int:
        MOD = 10**9 + 7

        def option(sub):
            if len(sub) == 1:
                if sub[0] == "0":
                    return 0
                return 9 if sub[0] == "*" else 1

            elif len(sub) == 2:
                # start with 0, 3 or more
                if sub[0] in "03456789":
                    return 0

                # start with 1
                elif sub[0] == "1":
                    return 9 if sub[1] == "*" else 1

                # start with 2
                elif sub[0] == "2":
                    if sub[1] == "*":
                        return 6
                    return 0 if sub[1] in "789" else 1

                # start with *
                elif sub[0] == "*":
                    if sub[1] == "*":
                        return 15
                    return 1 if sub[1] in "789" else 2

        @cache
        def dfs(i=0):
            if i >= len(s):
                return 1
            if i < len(s) - 1:
                rv = option(s[i]) * dfs(i + 1) + \
                    option(s[i:i + 2]) * dfs(i + 2)
            else:
                rv = option(s[i]) * dfs(i + 1)
            return rv % MOD
        return dfs() % MOD
# @lc code=end
