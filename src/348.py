# TAGS: Premium, Design
class TicTacToe:
    """
    556 ms, 5%. Time and Space: O(N^2)
    """
    # O(N^2)
    def __init__(self, n: int):
        self.board = [[0] * n for _ in range(n)]
        self.N = n
    
    #O(N)
    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        self.board[row][col] = player
        if self.check_winner(row, col, player):
            return player
        return 0
    
    # O(N)
    def check_winner(self, row, col, player):
        if sum(self.board[row][i] == player for i in range(self.N)) == self.N:
            return True
        if sum(self.board[i][col] == player for i in range(self.N)) == self.N:
            return True
        if sum(self.board[i][i] == player for i in range(self.N)) == self.N:
            return True
        if sum(self.board[i][~i] == player for i in range(self.N)) == self.N:
            return True
        return False
    
class TicTacToe:
    """
    Time: O(1). Space: O(N^2). 100 ms, 31.7%.
    """
    # O(1)
    def __init__(self, n: int):
        self.counter = collections.Counter()
        self.N = n
        
    #O(1)
    def move(self, row: int, col: int, player: int) -> int:
        for i, x in enumerate((row, col, row - col, row + col)):
            self.counter[(i, x, player)] += 1
            if self.counter[(i, x, player)] == self.N:
                return player
        return 0

class TicTacToe:
    """
    Time: O(1). Space: O(N^2). 84 ms, 81.62%. Same as above but Pythonic
    """
    # O(1)
    def __init__(self, n: int):
        self.counter = collections.Counter()
        def move(row, col, player):
            for i, x in enumerate((row, col, row - col, row + col)):
                self.counter[(i, x, player)] += 1
                if self.counter[(i, x, player)] == n:
                    return player
            return 0    
        self.move = move
        
        
    
# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)