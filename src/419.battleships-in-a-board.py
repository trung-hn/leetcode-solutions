#
# @lc app=leetcode id=419 lang=python3
#
# [419] Battleships in a Board
#

# @lc code=start
# TAGS: Array, Depth First Search
# REVIEWME: Think about head (or tail) of the ships
class Solution:
    # 76 ms, 58.48%. O(N*N), O(1)
    def countBattleships(self, board: List[List[str]]) -> int:
        if not board: return 0
        def sink(r, c):
            board[r][c] = "."
            for x, y in ((r, c - 1), (r, c + 1), (r - 1, c), (r + 1, c)):
                if 0 <= x < R and 0 <= y < C and board[x][y] == "X":
                    sink(x, y)
            return True
        R, C = len(board), len(board[0])
        return sum(sink(r, c) for r in range(R) for c in range(C) if board[r][c] == "X")
    
    # 68 ms, 93.11%. O(N*N). O(1). 1 Pass. Better solution
    def countBattleships(self, board: List[List[str]]) -> int:
        """
        Explanation: we only need to check if the cell to the top and to the left are empty.
        """
        if not board: return 0
        cnt = 0
        R, C = len(board), len(board[0])
        for r in range(R):
            for c in range(C):
                if board[r][c] == "X":
                    cnt += (c == 0 or board[r][c-1] != "X") and (r == 0 or board[r-1][c] != "X")
        return cnt
# @lc code=end

