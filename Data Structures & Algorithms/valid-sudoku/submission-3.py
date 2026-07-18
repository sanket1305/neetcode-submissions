class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9

        rows = [0] * N
        cols = [0] * N
        boxes = [0] * 9

        for r in range(N):
            for c in range(N):
                # skip if no number
                if board[r][c] == '.':
                    continue
                
                pos = int(board[r][c]) - 1  # 0-index

                if rows[r] & (1 << pos):
                    return False
                rows[r] |= (1 << pos)

                if cols[c] & (1 << pos):
                    return False
                cols[c] |= (1 << pos)

                idx = (r // 3) * 3 + (c // 3)
                if boxes[idx] & (1 << pos):
                    return False
                boxes[idx] |= (1 << pos)
        
        return True