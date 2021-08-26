#
# @lc app=leetcode id=633 lang=python3
#
# [633] Sum of Square Numbers
#

# @lc code=start
# TAGS: Math, Two Pointers, Binary Search


class Solution:
    # Time: O(logN). Space: O(logN)
    def judgeSquareSum(self, c: int) -> bool:
        squares = set(n*n for n in range(int(c**0.5) + 1))

        for square in squares:
            if square <= c and (c - square) in squares:
                return True
        return False
# @lc code=end
