#
# @lc app=leetcode id=581 lang=python3
#
# [581] Shortest Unsorted Continuous Subarray
#

# @lc code=start
# TAGS: Array
class Solution:
    # 216 ms, 83 %. O(NlogN)
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        start = end = -1
        for i in range(len(nums)):
            if nums[i] != sorted_nums[i]:
                if start == -1:
                    start = i
                end = i
        return 0 if start == end == -1 else end - start + 1
    
    # 196 ms, 81.96%. Time: O(N). Space: O(1)
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # Find right limit of the subarray. Traverse array from left to right
        right_ptr = 0
        big = nums[0]
        for i in range(len(nums)):
            if nums[i] < big:
                right_ptr = i
            else:
                big = nums[i]
        
        # Find left limit of the subarray.Traverse array from right to left
        left_ptr = 0
        small = nums[-1]
        for i in reversed(range(len(nums))):
            if nums[i] > small:
                left_ptr = i
            else:
                small = nums[i]
                
        if right_ptr == left_ptr: return 0
        return right_ptr - left_ptr + 1
    
# @lc code=end

