#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#

# @lc code=start
# TAGS: Array
class Solution:
    # 56 ms, Time and Space: O(N^2)
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0]*n for _ in range(n)]
        delta = [[0, 1], [1, 0], [0, -1],[-1, 0]]
        ptr = x = y = 0
        for i in range(1, n**2 + 1):
            matrix[x][y] = i
            new_x = x + delta[ptr][0]
            new_y = y + delta[ptr][1]
            if not (0 <= new_x < n and 0 <= new_y < n and matrix[new_x][new_y] == 0):
                ptr = (ptr + 1) % 4
            x += delta[ptr][0]
            y += delta[ptr][1]
        return matrix
        
# @lc code=end

