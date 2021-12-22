#
# @lc app=leetcode id=85 lang=python3
#
# [85] Maximal Rectangle
#

# @lc code=start
# TAGS: Array, Dynamic Programming, Stack, Matrix, Monotonic Stack
# REVIEWME: Dynamic Programming, Monotonic Stack
class Solution:
    # 288 ms, 36.74%. Time: O(R*C*C). Space: O(C)
    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        # Exactly same as #84
        def get_max_area(row):
            row += [-1]
            ans = 0
            stack = [-1]
            for i, val in enumerate(row):
                while stack and row[stack[-1]] > val:
                    curr = stack.pop()
                    left = stack[-1]
                    right = i
                    ans = max(ans, row[curr] * (right - left - 1))
                stack.append(i)
            return ans

        matrix = [[int(val) for val in row] for row in matrix]
        ans = 0
        R, C = len(matrix), len(matrix[0])
        for r in range(R):
            for c in range(C):
                if r > 0 and matrix[r][c]:
                    matrix[r][c] += matrix[r - 1][c]
            ans = max(ans, get_max_area(matrix[r]))
        return ans


# @lc code=end
