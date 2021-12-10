#
# @lc app=leetcode id=2000 lang=python3
#
# [2000] Reverse Prefix of Word
#

# @lc code=start
# TAGS: Two Pointers, String
class Solution:
    # 24 ms, 96.39%. Time: O(N). Space: O(1)
    def reversePrefix(self, word: str, ch: str) -> str:
        for i, c in enumerate(word):
            if c == ch:
                return word[:i + 1][::-1] + word[i + 1:]
        return word
# @lc code=end
