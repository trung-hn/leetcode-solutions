#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
# TAGS: Array, Two Pointers


class Solution:
    # Time: O(N). Space: O(1)
    def moveZeroes(self, nums):
        zero = 0  # records the position of "0"
        for i in range(len(nums)):
            if nums[i]:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1

    # Time: O(N). Space: O(1)
    def moveZeroes(self, nums):
        zero = 0
        for n_zero in range(len(nums)):

            # Swap if  zero is zero and non_zero is non zero
            if not nums[zero] and nums[n_zero]:
                nums[zero], nums[n_zero] = nums[n_zero], nums[zero]

            # Move zero index if one of thw two is non zero
            if nums[zero] or nums[n_zero]:
                zero += 1


# @lc code=end
