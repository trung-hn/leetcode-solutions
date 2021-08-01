#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
# TAGS: Array, Two Pointers, Greedy
from _typeshed import HasFileno


class Solution:
    # Time: O(N^2). Space: O(1)
    def maxArea(self, height: List[int]) -> int:
        result = 0
        for left in range(len(height)):  # O(N)
            for right in range(left + 1, len(height)):  # O(N)
                area = min(height[left], height[right]) * (right - left)
                result = max(result, area)
        return result

    # Time: O(N). Space: O(1)
    def maxArea(self, height: List[int]) -> int:
        result = left = 0
        right = len(height) - 1
        while left < right:  # O(N)
            result = max(result, min(
                height[left], height[right]) * (right - left))
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return result
# @lc code=end
