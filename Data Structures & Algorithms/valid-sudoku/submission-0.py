class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9

        row = [set() for i in range(n)]
        col = [set() for i in range(n)]
        grid = [set() for i in range(n)]
    
        for r in range(n):
            for c in range(n):
                ele = board[r][c]

                if ele == ".":
                    continue

                if ele in row[r]:
                    return False
                row[r].add(ele)

                if ele in col[c]:
                    return False
                col[c].add(ele)

                idx = (r//3)*3 + c//3
                if ele in grid[idx]:
                    return False
                grid[idx].add(ele)
        
        return True