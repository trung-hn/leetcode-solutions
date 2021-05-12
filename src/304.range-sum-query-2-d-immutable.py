#
# @lc app=leetcode id=304 lang=python3
#
# [304] Range Sum Query 2D - Immutable
#

# @lc code=start
# TAGS: Dynamic Programming
# REVIEWME: Matrix


class NumMatrix:
    """
    Init time: O(R*C)
    Query time: O(1)
    """

    def __init__(self, matrix: List[List[int]]):
        R, C = len(matrix), len(matrix[0])
        self.matrix = [[0]*(C+1) for _ in range(R+1)]

        # Cummulate from left to right
        for c in range(C):
            for r in range(R):
                self.matrix[r + 1][c + 1] = self.matrix[r + 1][c] \
                    + matrix[r][c]

        # Cummulate from top to bottom
        for c in range(C):
            for r in range(R):
                self.matrix[r+1][c+1] += self.matrix[r][c+1]

        # Cleaner way to setup matrix:
        # for c in range(C):
        #     for r in range(R):
        #         self.matrix[r + 1][c + 1] = self.matrix[r][c + 1] \
        #             + self.matrix[r + 1][c] \
        #             + matrix[r][c] \
        #             - self.matrix[r][c]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.matrix[row2 + 1][col2 + 1] \
            - self.matrix[row1][col2 + 1] \
            - self.matrix[row2 + 1][col1] \
            + self.matrix[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# @lc code=end
