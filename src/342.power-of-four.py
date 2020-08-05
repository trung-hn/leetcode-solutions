#
# @lc app=leetcode id=342 lang=python3
#
# [342] Power of Four
#

# @lc code=start
# TAGS: Math, Bit Manipulation
class Solution:
    # 56 ms, 10.52%. Time: O(logN). Space: O(1)
    def isPowerOfFour(self, num: int) -> bool:
        while num > 1:
            num /= 4
        return num == 1

    # There are several O(1) solutions in the articles
    # Time and Soace: O(1)
    def isPowerOfFour(self, num: int) -> bool:
        return num > 0 and math.log2(num) % 2  == 0

# @lc code=end

