#
# @lc app=leetcode id=171 lang=python3
#
# [171] Excel Sheet Column Number
#

# @lc code=start
# TAGS: String
class Solution:
    # 20 ms, 99%. Time: O(N), Space: O(1)
    def titleToNumber(self, s: str) -> int:
        total = 0
        for i, c in enumerate(s):
            total += (ord(c) - ord("A") + 1) * 26 ** (len(s) - i - 1)
        return total

# @lc code=end

