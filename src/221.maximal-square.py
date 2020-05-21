#
# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
#

# @lc code=start
# TAGS: Array, Dynamic Programming
# REVIEWME: similar to 1277
class Solution:
    # 184 ms, 97.47%. O(M*N) Similar to best solution. 
    # The idea is very simple, it is a greedy approach by calculating the tail based on the cells it depends on to make a square
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]: return 0
        matrix = [[1 if c == '1' else 0 for c in row] for row in matrix]
        R, C = len(matrix), len(matrix[0])
        
        # Calculate tail. 
        for r in range(1, R):
            for c in range(1, C):
                if matrix[r][c]:
                    matrix[r][c] = min(matrix[r - 1][c], matrix[r][c - 1], matrix[r - 1][c - 1]) + 1
                    
        # Get max tail.
        mx = max(v for row in matrix for v in row)
        return mx ** 2
# @lc code=end

