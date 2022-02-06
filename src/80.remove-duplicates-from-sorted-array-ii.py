#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#

# @lc code=start
# TAGS: Array, Two Pointers
from typing import List


class Solution:
    # 89 ms, 30.19%. Time: O(N). Space: O(1)
    def removeDuplicates(self, nums: List[int]) -> int:
        ptr = 0
        for n in nums:
            if ptr < 2 or n != nums[ptr - 2]:
                nums[ptr] = n
                ptr += 1
        return ptr
# @lc code=end
