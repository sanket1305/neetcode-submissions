class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # process top and bottom row first
        q = deque()

        for col in range(cols):
            for row in [0, rows - 1]:
                if grid[row][col] == 1:
                    grid[row][col] = 0
                    q.append((row, col))

        # process first and last col first
        for row in range(rows):
            for col in [0, cols - 1]:
                if grid[row][col] == 1:
                    grid[row][col] = 0
                    q.append((row, col))
        
        while q:
            row, col = q.popleft()

            for dr, dc in directions:
                nr, nc = row + dr, col + dc

                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 0
                    q.append((nr, nc))
        
        res = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    res += 1
        
        return res