#
# @lc app=leetcode id=1277 lang=python3
#
# [1277] Count Square Submatrices with All Ones
#

# @lc code=start
# TAGS: Array, Dynamic Programming
class Solution:
    # 644 ms, 86.64%
    # Exactly the same as problem 221
    def countSquares(self, matrix: List[List[int]]) -> int:
        for r in range(1, len(matrix)):
            for c  in range(1, len(matrix[0])):
                if matrix[r][c]:
                    matrix[r][c] = min(matrix[r-1][c-1], matrix[r][c-1], matrix[r-1][c]) + 1
        return sum(val for row in matrix for val in row)
        
# @lc code=end

