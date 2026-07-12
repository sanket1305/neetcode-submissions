class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    edges = 4

                    if row - 1 >= 0 and grid[row - 1][col] == 1:
                        edges -= 1
                    if col - 1 >= 0 and grid[row][col - 1] == 1:
                        edges -= 1
                    if row + 1 < rows and grid[row + 1][col] == 1:
                        edges -= 1
                    if col + 1 < cols and grid[row][col + 1] == 1:
                        edges -= 1
                    
                    res += edges
        
        return res