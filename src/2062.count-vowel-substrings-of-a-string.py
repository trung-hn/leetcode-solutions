#
# @lc app=leetcode id=2062 lang=python3
#
# [2062] Count Vowel Substrings of a String
#

# @lc code=start
# TAGS: Hash Table, String

class Solution:
    # Time: O(N^3). Space: O(N)
    def countVowelSubstrings(self, word: str) -> int:
        def is_valid(sub):
            return set(sub) == set("aeoui")

        cnt = 0
        for i in range(len(word)):
            for j in range(i + 1, len(word) + 1):
                sub = word[i:j]
                cnt += is_valid(sub)
        return cnt
# @lc code=end
