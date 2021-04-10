#
# @lc app=leetcode id=329 lang=python3
#
# [329] Longest Increasing Path in a Matrix
#

# @lc code=start
# TAGS: DFS, Topology Sort, Memoization
# REVIEWME: Memoization


class Solution:
    # First solution with custom memo:
    # 476 ms, 64.96%. Time and Space: O(R*C)
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        visited = {}

        def dfs(r, c):
            if (r, c) in visited:
                return visited[(r, c)]
            rv = 0
            path_exists = False
            for x, y in (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1):
                if 0 <= x < R and 0 <= y < C and matrix[x][y] > matrix[r][c]:
                    rv = max(rv, dfs(x, y))
                    path_exists = True
            visited[(r, c)] = rv + path_exists
            return visited[(r, c)]

        R, C = len(matrix), len(matrix[0])
        return max(dfs(r, c) for r in range(R) for c in range(C)) + 1

    # 432 ms, 82.40%. Time and Space: O(R*C). Clean solution
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        @cache
        def dfs(r, c):
            rv = 0
            for x, y in (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1):
                if 0 <= x < R and 0 <= y < C and matrix[x][y] > matrix[r][c]:
                    rv = max(rv, dfs(x, y) + 1)
            return rv

        R, C = len(matrix), len(matrix[0])
        return max(dfs(r, c) for r in range(R) for c in range(C)) + 1
# @lc code=end
