#
# @lc app=leetcode id=795 lang=python3
#
# [795] Number of Subarrays with Bounded Maximum
#

# @lc code=start
# TAGS: Array
# REVIEWME: Array


class Solution:
    """
    Approach:
    Increase counter based on current value linearly.
    If num < left, we can only append to current subarrays
    If left < num < right, we have (i - prev) more subarrays from previous invalid num
    if right < num, reset ptr 
    """
    # 320 ms, 94.21%. Time: O(N). Space: O(1)

    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        total = curr = 0
        prev = -1
        for i, num in enumerate(nums):
            if left <= num <= right:
                # Number of subarray between prev (invalid) and curr num
                curr = i - prev
                # Increase total
                total += curr
            elif num < left:
                # Append to the end of all subarray from last prev (invalid)
                total += curr
            elif right < num:
                # Reset prev and curr no of subarrays
                curr = 0
                prev = i
        return total
# @lc code=end
