#
# @lc app=leetcode id=2042 lang=python3
#
# [2042] Check if Numbers Are Ascending in a Sentence
#

# @lc code=start
# TAGS: String


class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        prev = 0
        for w in s.split():
            if not w.isdigit():
                continue
            if int(w) > prev:
                prev = int(w)
            else:
                return False
        return True
# @lc code=end
