#
# @lc app=leetcode id=1837 lang=python3
#
# [1837] Sum of Digits in Base K
#

# @lc code=start
# TAGS: Math, Bit Manipulation


class Solution:
    # 28 ms, 85.83%. Time: O(logN). Space: O(1)
    def sumBase(self, n: int, k: int) -> int:
        ans = 0
        while n >= k:
            n, r = divmod(n, k)
            ans += r
        return ans + n
# @lc code=end
