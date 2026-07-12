class Solution:
    def totalNQueens(self, n: int) -> int:
        res = []
        board = [['.'] * n for _ in range(n)]

        def backtrack(r):
            # r is row number and queen number
            if r == n:
                # means we have already placed all queens
                copy = [''.join(row) for row in board]
                res.append(copy)
                return
            
            # check for each cell, if it's safe to place queen
            for c in range(n):
                if self.isSafe(r, c, board):
                    # place queen in this cell
                    board[r][c] = "Q"

                    # call backtrack on next row, to explore any possible valid answers
                    backtrack(r + 1)

                    # remove queen from current cell
                    board[r][c] = "."
        
        backtrack(0)
        return len(res)

    def isSafe(self, r: int, c: int, board) -> bool:
        # check vertically up
        row = r-1
        while row >= 0:
            if board[row][c] == "Q":
                return False
            row -= 1
        
        # check left diagonal (top half)
        row, col = r-1, c-1
        while row >= 0 and col >= 0:
            if board[row][col] == "Q":
                return False
            row, col = row-1, col-1
        
        # check right diagonal (top right)
        row, col = r-1, c+1
        while row >= 0 and col < len(board):
            if board[row][col] == "Q":
                return False
            row, col = row-1, col+1
        
        return True