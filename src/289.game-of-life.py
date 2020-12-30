#
# @lc app=leetcode id=289 lang=python3
#
# [289] Game of Life
#

# @lc code=start
# TAGS: Array
class Solution:
    # 32 ms, 90%. Time and Space: O(M*N)
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board: return 
        def count(i, j):
            rv = 0
            for di in (-1, 0, 1):
                for dj in (-1, 0, 1):
                    if di == dj == 0: continue
                    if 0 <= i + di < R and 0 <= j + dj < C:
                        rv += board[i + di][j + dj]
            return rv
    
        R, C = len(board), len(board[0])
        ans = [[0]*C for _ in range(R)]
        for i in range(R):
            for j in range(C):
                ones = count(i, j)
                if board[i][j]:
                    ans[i][j] = 1 if 2 <= ones <= 3 else 0
                elif ones == 3: 
                    ans[i][j] = 1
        
        board[:] = ans
    
    # 32 ms, 90%. Time: O(M*N). Space: O(1)
    def gameOfLife(self, board: List[List[int]]) -> None:
        if not board: return 
        def count(i, j):
            rv = 0
            for di in (-1, 0, 1):
                for dj in (-1, 0, 1):
                    if di == dj == 0: continue
                    if 0 <= i + di < R and 0 <= j + dj < C:
                        if board[i + di][j + dj] in (-1, 1, 3):
                            rv += 1
            return rv
        
        R, C = len(board), len(board[0])
        for i in range(R):
            for j in range(C):
                ones = count(i, j)
                if board[i][j]:
                    board[i][j] = 3 if 2 <= ones <= 3 else -1
                else:
                    if ones == 3: board[i][j] = 2
                    
        for i in range(R):
            for j in range(C):
                board[i][j] = 0 if board[i][j] <= 0 else 1
        
# @lc code=end

