#
# @lc app=leetcode id=1465 lang=python3
#
# [1465] Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts
#

# @lc code=start
# TAGS: Array


class Solution:
    # 304 ms, 71.40%. Time: O(NlogN). Space: O(N)
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:

        # Sort and include the end points
        horizontalCuts.sort()
        verticalCuts.sort()
        horizontalCuts = [0] + horizontalCuts + [h]
        verticalCuts = [0] + verticalCuts + [w]

        # Find max height
        max_height = 0
        for h1, h2 in zip(horizontalCuts, horizontalCuts[1:]):
            max_height = max(max_height, h2 - h1)

        # Find max width
        max_width = 0
        for v1, v2 in zip(verticalCuts, verticalCuts[1:]):
            max_width = max(max_width, v2 - v1)

        return max_height * max_width % (10 ** 9 + 7)
# @lc code=end
