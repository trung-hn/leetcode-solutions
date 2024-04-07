#
# @lc app=leetcode id=3105 lang=python3
#
# [3105] Longest Strictly Increasing or Strictly Decreasing Subarray
#


# @lc code=start
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc = dec = ans = 1
        for n1, n2 in zip(nums, nums[1:]):
            if n1 > n2:
                dec += 1
                inc = 1
            elif n1 < n2:
                inc += 1
                dec = 1
            else:
                dec = inc = 1
            ans = max([ans, inc, dec])
        return ans


# @lc code=end
