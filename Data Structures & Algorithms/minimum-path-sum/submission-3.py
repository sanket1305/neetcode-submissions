class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        heap = [[grid[0][0], 0, 0]]
        seen = set()
        seen.add((0, 0))

        directions = [(1, 0), (0, 1)]

        while heap:
            print(heap)
            cost, r, c = heapq.heappop(heap)

            if r == (rows - 1) and c == (cols - 1):
                return cost
            seen.add((r, c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in seen:
                    new_cost = cost + grid[nr][nc]
                    seen.add((nr, nc))

                    heapq.heappush(heap, [new_cost, nr, nc])