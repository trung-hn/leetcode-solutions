#
# @lc app=leetcode id=2119 lang=python3
#
# [2119] A Number After a Double Reversal
#

# @lc code=start
class Solution:
    # 28 ms, 85.96%. Time and Space: O(1)
    def isSameAfterReversals(self, num: int) -> bool:
        if num == 0:
            return True
        return num % 10
# @lc code=end
