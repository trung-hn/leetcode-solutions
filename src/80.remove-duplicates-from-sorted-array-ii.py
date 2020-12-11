#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#

# @lc code=start
# TAGS: Array, Two Pointers
class Solution:
    # 44 ms, 97.91%. Time: O(N). Space: O(1)
    def removeDuplicates(self, nums: List[int]) -> int:
        L = len(nums)
        ptr = cnt = prev = 0
        for i, num in enumerate(nums):
            if num != prev: cnt = 1
            else: cnt += 1
            prev = num
            
            # Change to -1 in order to replace later.
            if cnt > 2: nums[i] = None
            
            # Increase ptr to where we can replace. 
            while ptr < i and nums[ptr] is not None: ptr += 1
            
            # Replace the number
            nums[i], nums[ptr] = nums[ptr], nums[i]
            
        try:
            return nums.index(None)
        except:
            return len(nums)

    # 44 ms, 97.91%. Same idea but clean solution from Stefan
    def removeDuplicates(self, nums):
        i = 0
        for n in nums:
            if i < 2 or n > nums[i-2]:
                nums[i] = n
                i += 1
        return i
# @lc code=end

