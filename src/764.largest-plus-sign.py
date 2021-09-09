#
# @lc app=leetcode id=764 lang=python3
#
# [764] Largest Plus Sign
#

# @lc code=start
# TAGS: Array, Dynamic Programming


class Solution:
    # 2458 ms, 82.70%.
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        # Init
        matrix = [[1] * n for _ in range(n)]
        for r, c in mines:
            matrix[r][c] = 0

        lefts = [[0] * n for _ in range(n)]
        rights = [[0] * n for _ in range(n)]
        ups = [[0] * n for _ in range(n)]
        downs = [[0] * n for _ in range(n)]

        # Calculate cummultive sum from left and right
        for r in range(n):
            left = right = 0
            for c in range(n):
                left = left + 1 if matrix[r][c] else 0
                right = right + 1 if matrix[r][~c] else 0
                lefts[r][c] = left
                rights[r][~c] = right

        # Calculate cummultive sum from up and down
        for c in range(n):
            up = down = 0
            for r in range(n):
                up = up + 1 if matrix[r][c] else 0
                down = down + 1 if matrix[~r][c] else 0
                ups[r][c] = up
                downs[~r][c] = down

        return max(min(lefts[r][c], rights[r][c], ups[r][c], downs[r][c])
                   for r in range(n)
                   for c in range(n))

# @lc code=end
