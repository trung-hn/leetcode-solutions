#
# @lc app=leetcode id=665 lang=python3
#
# [665] Non-decreasing Array
#

# @lc code=start
# TAGS: Array
# REVIEWME: Array


class Solution:
    """
    Approach:
    When we see a decrease in value, there 2 ways to fix it:
    change prev to after
    change after to prev
    Try both cases and check cnt at the end
    """
    # 176 ms, 89.39%. Time: O(N). Space: O(1)

    def checkPossibility(self, nums: List[int]) -> bool:
        cnt = 0
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                cnt += 1
                if i < 2 or nums[i - 2] <= nums[i]:
                    nums[i - 1] = nums[i]
                else:
                    nums[i] = nums[i - 1]
        return cnt <= 1

# @lc code=end
