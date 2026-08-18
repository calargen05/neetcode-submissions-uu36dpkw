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
        interval = len(queue)
        while queue:
            for i in range(interval):
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    if 0 <= nr < rows and 0 <= nc < columns and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr, nc))
            interval = len(queue)
            time += 1
        
        print(time)
        if fresh > 0:
            return -1
        else:
            return time - 1
