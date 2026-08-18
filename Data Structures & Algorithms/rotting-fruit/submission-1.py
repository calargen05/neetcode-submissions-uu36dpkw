class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, columns = len(grid), len(grid[0])
        fresh, queue = 0, deque()

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append((r,c))
        
        if fresh == 0:
            return 0
        if not queue:
            return -1

        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        time = 0
        while queue and fresh > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    if 0 <= nr < rows and 0 <= nc < columns and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr, nc))
            time += 1
        

        return time if not fresh else -1
