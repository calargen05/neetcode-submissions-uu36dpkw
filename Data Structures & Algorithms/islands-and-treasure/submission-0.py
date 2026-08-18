class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        rows, columns = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 0:
                    queue.append((r,c))
        
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        level = 1
        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < columns and grid[nr][nc] == 2147483647:
                    grid[nr][nc] = grid[r][c] + 1
                    queue.append((nr, nc))

            level += 1