#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
# TAGS: Tricky
class Solution:
    # 32 ms. 60.66%
    # Note that `<<`` does not take priority over `-`. 
    # This means (1<<31) - 1 != (1<<31 - 1)
    # Use input to test this
    def reverse(self, x: int) -> int:
        ans = -int(str(-x)[::-1]) if x < 0 else int(str(x)[::-1])
        return ans if (-1<<31) <= ans <= ((1<<31) - 1) else 0
# @lc code=end

