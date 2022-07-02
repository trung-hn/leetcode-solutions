#
# @lc app=leetcode id=2270 lang=python3
#
# [2270] Number of Ways to Split Array
#

# @lc code=start
# TAGS: Array, Prefix Sum
from typing import List


class Solution:
    # Time and SPace: O(N)
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefix_sum = nums.copy()
        for i in range(1, len(nums)):
            prefix_sum[i] += prefix_sum[i - 1]

        cnt = 0
        for i in range(len(nums) - 1):
            left = prefix_sum[i]
            right = prefix_sum[-1] - prefix_sum[i]
            if left >= right:
                cnt += 1
        return cnt


# @lc code=end
