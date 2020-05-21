#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
# TAGS: Binary Search
# REVIEWME:
class Solution:
    # 44 ms, 45%. O(log N), O(1)
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]: return nums[0]
        
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi)//2
            val = nums[mid]
            if val < nums[hi]:
                hi = mid
            else:
                lo = mid + 1
        return nums[lo]
# @lc code=end

