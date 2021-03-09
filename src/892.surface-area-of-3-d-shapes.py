#
# @lc app=leetcode id=892 lang=python3
#
# [892] Surface Area of 3D Shapes
#

# @lc code=start
# TAGS: Math, Geometry


class Solution:
    # 76 ms, 97.49%. Time: O(N*N). Space: O(1)
    def surfaceArea(self, grid: List[List[int]]) -> int:
        top = sum(val > 0 for row in grid for val in row)

        total = 2 * top
        for row in grid:
            total += row[0] + row[-1]
            for n1, n2 in zip(row, row[1:]):
                total += abs(n2 - n1)

        for col in zip(*grid):
            total += col[0] + col[-1]
            for n1, n2 in zip(col, col[1:]):
                total += abs(n2 - n1)
        return total
# @lc code=end
