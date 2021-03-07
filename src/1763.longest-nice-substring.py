#
# @lc app=leetcode id=1763 lang=python3
#
# [1763] Longest Nice Substring
#

# @lc code=start
# TAGS: String


class Solution:
    # 32 ms, 100%. Time: O(NlogN). Space: O(N). Divide and Conquer
    def longestNiceSubstring(self, s: str) -> str:
        def dfs(start, end):
            chars = set(s[start: end])
            for i in range(start, end):
                if s[i].upper() in chars and s[i].lower() in chars:
                    continue
                s1 = dfs(start, i)
                s2 = dfs(i + 1, end)
                return s1 if len(s1) >= len(s2) else s2
            return s[start:end]
        return dfs(0, len(s))
# @lc code=end
