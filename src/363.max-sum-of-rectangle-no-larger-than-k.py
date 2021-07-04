#
# @lc app=leetcode id=363 lang=python3
#
# [363] Max Sum of Rectangle No Larger Than K
#

# @lc code=start
# TAGS: Array, Binary Search, Dynamic Programming, Matrix, Ordered Set
# REVIEWME: Ordered Set
import sortedcontainers


class Solution:
    # LTE. Time: O(R*R*C*C)
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        R, C = len(matrix), len(matrix[0])
        prefix_mat = [[0] * (C + 1)]

        for row in matrix:
            temp = [0]
            for val in row:
                temp.append(temp[-1] + val)
            prefix_mat.append(temp)

        for c in range(1, C + 1):
            for r in range(1, R + 1):
                prefix_mat[r][c] += prefix_mat[r - 1][c]

        ans = float("-inf")
        for r in range(1, R + 1):
            for c in range(1, C + 1):
                for nr in range(r, R + 1):
                    for nc in range(c, C + 1):
                        val = prefix_mat[nr][nc] \
                            - prefix_mat[nr][c - 1] \
                            - prefix_mat[r - 1][nc] \
                            + prefix_mat[r - 1][c - 1]
                        if val > ans and val <= k:
                            ans = val
        return ans

    # 7552 ms, 5.09%. Time: O(R*R*C*logC). Space: O(R*C)
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:

        R, C = len(matrix), len(matrix[0])

        # Create prefix sum matrix
        prefix_mat = [[0] * (C + 1)]
        for row in matrix:
            temp = [0]
            for val in row:
                temp.append(temp[-1] + val)
            prefix_mat.append(temp)

        for c in range(1, C + 1):
            for r in range(1, R + 1):
                prefix_mat[r][c] += prefix_mat[r - 1][c]

        # Try different matrix size (by adjusting rows)
        ans = float("-inf")
        for r1 in range(0, R):
            for r2 in range(r1 + 1, R + 1):
                visited = sortedcontainers.SortedList([])

                # Loop through each column
                for c in range(C + 1):

                    # sum of this rectangle
                    cumm_val = prefix_mat[r2][c] - prefix_mat[r1][c]

                    # binarysearch visited to find value such that cumm_val - val near K
                    index = visited.bisect_left(cumm_val - k)
                    if index < len(visited) and k < cumm_val - visited[index]:
                        index += 1
                    if index < len(visited):
                        ans = max(ans, cumm_val - visited[index])

                    # add current cumm_val to visited
                    visited.add(cumm_val)
        return ans
# @lc code=end
