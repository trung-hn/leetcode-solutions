#
# @lc app=leetcode id=540 lang=python3
#
# [540] Single Element in a Sorted Array
#

# @lc code=start
# TAGS: Binary Search,
class Solution:
    # 80 ms, 22.6 %. O(log N). O(1)
    def singleNonDuplicate(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums)//2
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[2*mid] == nums[2*mid + 1]:
                lo = mid + 1
            else:
                hi = mid
        return nums[lo*2]
# @lc code=end

