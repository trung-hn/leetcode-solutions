#
# @lc app=leetcode id=1752 lang=python3
#
# [1752] Check if Array Is Sorted and Rotated
#

# @lc code=start
# TAGS: Array


class Solution:
    # 36 ms, 51.30 %. Time: O(N). Space: O(1)
    def check(self, nums: List[int]) -> bool:
        cnt = sum(n1 > n2 for n1, n2 in zip(nums, nums[1:]))
        if nums[0] >= nums[-1]:
            return cnt <= 1
        return cnt == 0

    # Cleaner solution
    def check(self, nums: List[int]) -> bool:
        return sum(nums[i] < nums[i-1] for i in range(len(nums))) <= 1
# @lc code=end
