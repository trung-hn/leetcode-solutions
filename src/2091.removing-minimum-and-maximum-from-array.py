#
# @lc app=leetcode id=2091 lang=python3
#
# [2091] Removing Minimum and Maximum From Array
#

# @lc code=start
# TAGS: Greedy, Array
from typing import List


class Solution:
    # Time: O(N). Space: O(1)
    def minimumDeletions(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        max_arg = nums.index(max(nums))
        min_arg = nums.index(min(nums))

        op1 = max(max_arg, min_arg) + 1
        op2 = len(nums) - min(max_arg, min_arg)
        op3 = min(min_arg, max_arg) + 1 + len(nums) - max(max_arg, min_arg)
        return min(op1, op2, op3)
# @lc code=end
