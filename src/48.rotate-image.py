#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start
# TAGS: Array


class Solution:
    """
    Approach:
    Vertical flip and then transpose
    """
    # 32 ms, 82.10%. Time: O(N*M). Space: O(1)

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def vert_flip_me(matrix):
            for i in range(len(matrix) // 2):
                matrix[i], matrix[~i] = matrix[~i], matrix[i]

        def transpose_me(matrix):
            for i in range(len(matrix)):
                for j in range(i + 1, len(matrix)):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        vert_flip_me(matrix)
        transpose_me(matrix)

# @lc code=end
