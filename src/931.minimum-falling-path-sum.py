#
# @lc app=leetcode id=931 lang=python3
#
# [931] Minimum Falling Path Sum
#

# @lc code=start
# TAGS: Array, Dynamic Programming, Matrix
class Solution:
    # Time: O(R*C). Space: O(C)

    # Inplace 128ms. 67%
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        R, C = len(matrix), len(matrix[0])
        for r in range(1, R):
            for c in range(C):
                min_value = float("inf")
                for dc in [-1, 0, 1]:
                    nc = c + dc
                    if nc < 0  or nc >= R:
                        continue
                    min_value = min(min_value, matrix[r - 1][nc])
                matrix[r][c] += min_value
        return min(matrix[-1])

    # DP
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        dp = matrix[0]
        for row in matrix[1:]:
            tmp = []
            for c, cur in enumerate(row):
                min_value = min(dp[c + dc] for dc in (-1, 0, 1) if 0 <= c + dc < len(dp))
                tmp.append(cur + min_value)
            dp = tmp
        return min(dp)
# @lc code=end

