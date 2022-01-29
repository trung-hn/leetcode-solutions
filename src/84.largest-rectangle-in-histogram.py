#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#

# @lc code=start
# TAGS: Array, Stack, Monotonic Stack
# REVIEWME: Monotonic Stack
from typing import List


class Solution:
    # 836 ms, 61.07%. Time and Space: O(N)
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        The stack maintain the indexes of buildings with ascending height. 
        Before adding a new building pop the building who is taller than the new one. 
        The building popped out represent the height of a rectangle with the new building as the right boundary and the current stack top as the left boundary. 
        Calculate its area and update ans of maximum area. Boundary is handled using dummy buildings.
        """
        heights.append(-1)
        ans = 0
        stack = [-1]
        for i, val in enumerate(heights):
            while stack and heights[stack[-1]] > val:
                height = heights[stack.pop()]
                left = stack[-1]
                width = i - left - 1
                ans = max(ans, width * height)
            stack.append(i)
        return ans
# @lc code=end
