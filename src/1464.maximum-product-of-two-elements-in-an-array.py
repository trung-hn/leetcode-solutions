#
# @lc app=leetcode id=1464 lang=python3
#
# [1464] Maximum Product of Two Elements in an Array
#

# @lc code=start
class Solution:
    # 52 ms, 85.11%. Time: O(N). Space: O(1)
    def maxProduct(self, nums: List[int]) -> int:
        lo, hi = nums[:2]
        if lo > hi:
            lo, hi = hi, lo
        for i in range(2, len(nums)):
            if nums[i] > lo:
                lo = nums[i]
                if lo > hi:
                    lo, hi = hi, lo
        return (lo - 1) * (hi - 1)
# @lc code=end

