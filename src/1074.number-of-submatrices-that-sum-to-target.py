#
# @lc app=leetcode id=1074 lang=python3
#
# [1074] Number of Submatrices That Sum to Target
#

# @lc code=start
# TAGS: Array, Dynamic Programming, Sliding Window
# REVIEWME: Array, Dynamic Programming, Sliding Window


class Solution:
    """
    Approach:
    A harder version of #560.A bit tricky to wrap your head around.
    First, cummulate both row and col into a matrix
    Second, iterate over either row or column and keep track of visited. 
    """
    # 932 ms, 64.48%. Time: O(R*R*C). Space: O(R*C)

    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        R, C = len(matrix), len(matrix[0])
        prefix_sum = [[0] * (C + 1) for _ in range(R + 1)]
        # cummulative sum by row
        for r in range(R):
            for c in range(C):
                prefix_sum[r + 1][c + 1] = prefix_sum[r + 1][c] + matrix[r][c]

        # cummulative sum by col
        for c in range(C):
            for r in range(R):
                prefix_sum[r + 1][c + 1] += prefix_sum[r][c + 1]

        total = 0
        for r2 in range(R + 1):
            for r1 in range(r2):
                visited = collections.defaultdict(int)
                for c in range(C + 1):
                    cur = prefix_sum[r2][c] - prefix_sum[r1][c]
                    total += visited[cur]
                    visited[target + cur] += 1
        return total
# @lc code=end
