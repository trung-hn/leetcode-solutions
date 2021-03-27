#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
# TAGS: Array, Two Pointers, Binary Search


class Solution:
    """
    For the follow up questions, we can perform binary search on prefix sum array
    """
    # 72 ms, 78.04%. Time: O(N). Space: O(1)

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        result = len(nums) + 1
        ptr = sofar = 0
        for i, n in enumerate(nums):
            sofar += n
            while sofar >= target:
                result = min(result, i - ptr + 1)
                sofar -= nums[ptr]
                ptr += 1
        return result if result <= len(nums) else 0  # @lc code=end
