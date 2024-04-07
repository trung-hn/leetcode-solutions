#
# @lc app=leetcode id=3107 lang=python3
#
# [3107] Minimum Operations to Make Median of Array Equal to K
#


# @lc code=start
import bisect


class Solution:
    # Time: O(NlogN). Space: O(N)
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        nums.sort()
        mid = len(nums) // 2
        index = bisect.bisect(nums, k)
        if index <= mid:
            return sum(num - k for num in nums[index : mid + 1])
        return sum(k - num for num in nums[mid:index])


# @lc code=end
