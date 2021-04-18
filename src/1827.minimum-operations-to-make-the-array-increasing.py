#
# @lc app=leetcode id=1827 lang=python3
#
# [1827] Minimum Operations to Make the Array Increasing
#

# @lc code=start


class Solution:
    # 136 ms, 100%. Time: O(N). Space: O(1)
    def minOperations(self, nums: List[int]) -> int:
        total = 0
        for i in range(1, len(nums)):
            if nums[i - 1] >= nums[i]:
                total += nums[i - 1] - nums[i] + 1
                nums[i] = nums[i - 1] + 1
        return total
# @lc code=end
