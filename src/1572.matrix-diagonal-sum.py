#
# @lc app=leetcode id=1572 lang=python3
#
# [1572] Matrix Diagonal Sum
#

# @lc code=start
# TAGS: Array
class Solution:
    # 104 ms, 96.75%. Time: O(N). Space: O(1)
    def diagonalSum(self, mat: List[List[int]]) -> int:
        N = len(mat)
        total = - mat[N//2][N//2] if N % 2 else 0
        for i in range(N):
            total += mat[i][i] + mat[i][~i]
        return total

# @lc code=end

