#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#

# @lc code=start
# TAGS: Array, BFS, DFS, Union Find, Matrix


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        R, C = len(board), len(board[0])

        def dfs(r, c):
            if 0 <= r < R and 0 <= c < C and board[r][c] == "O":
                board[r][c] = "N"
                dfs(r+1, c)
                dfs(r-1, c)
                dfs(r, c+1)
                dfs(r, c-1)

        for r in range(R):
            for c in range(C):
                if r in (0, R - 1) or c in (0, C - 1):
                    if board[r][c] == "O":
                        dfs(r, c)

        board[:] = [['XO'[c == 'N'] for c in row] for row in board]

# @lc code=end
