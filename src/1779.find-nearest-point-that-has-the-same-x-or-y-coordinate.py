#
# @lc app=leetcode id=1779 lang=python3
#
# [1779] Find Nearest Point That Has the Same X or Y Coordinate
#

# @lc code=start
# TAGS: Array


class Solution:
    # 700 ms, 91.74%. Time: O(N). Space: O(1)
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        dist = float("inf")
        ptr = None
        for i, (px, py) in enumerate(points):
            if px != x and py != y:
                continue
            if abs(px - x) + abs(py - y) < dist:
                dist = abs(px - x) + abs(py - y)
                ptr = i
        return -1 if ptr is None else ptr
# @lc code=end
