#
# @lc app=leetcode id=1768 lang=python3
#
# [1768] Merge Strings Alternately
#

# @lc code=start
# TAGS: String


class Solution:
    # 20 ms, 100%. Time and Space: O(N)
    def mergeAlternately(self, word1: str, word2: str) -> str:
        rv = ""
        i = 0
        while i < len(word1) and i < len(word2):
            rv += word1[i] + word2[i]
            i += 1
        return rv + word1[i:] + word2[i:]
# @lc code=end
