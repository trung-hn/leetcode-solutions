#
# @lc app=leetcode id=1476 lang=python3
#
# [1476] Subrectangle Queries
#

# @lc code=start
# TAGS: Design
class SubrectangleQueries:
    """
    272 ms, 44.90 %
    """
    
    # Time: O(1). Space: O(1)
    def __init__(self, rectangle: List[List[int]]):
        self.rect = rectangle

    # Time: O(M*N). Space: O(1)
    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for r in range(row1, row2 + 1):
            for c in range(col1, col2 + 1):
                self.rect[r][c] = newValue

    # Time: O(1). Space: O(1)
    def getValue(self, row: int, col: int) -> int:
        return self.rect[row][col]

class SubrectangleQueries1:
    """
    160 ms, 96.14%. 
    """
    # Time: O(1). Space: O(N)
    def __init__(self, rectangle: List[List[int]]):
        self.rect = rectangle
        self.history = []

    # Time: O(1). Space: O(1)
    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        self.history.append((row1, col1, row2, col2, newValue))

    # Time: O(len(hist)). Space: O(1)
    def getValue(self, row: int, col: int) -> int:
        for row1, col1, row2, col2, newValue in reversed(self.history):
            if row1 <= row <= row2 and col1 <= col <= col2:
                return newValue
        return self.rect[row][col]


# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)
# @lc code=end

