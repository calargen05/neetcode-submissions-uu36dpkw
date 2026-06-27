class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        queue = deque()
        max_area = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    queue.append([i,j])
                    grid[i][j] = 0
                    area = 0
                    while queue:
                        coord = queue.popleft()
                        y,x = coord[0],coord[1]
                        area += 1

                        # check up
                        if y-1 >= 0:
                            if grid[y-1][x] == 1:
                                queue.append([y-1,x])
                                grid[y-1][x] = 0
                        
                        # check left
                        if x-1 >= 0:
                            if grid[y][x-1] == 1:
                                queue.append([y,x-1])
                                grid[y][x-1] = 0
                        
                        # check down
                        if y+1 < len(grid):
                            if grid[y+1][x] == 1:
                                queue.append([y+1,x])
                                grid[y+1][x] = 0
                        
                        # check right
                        if x+1 < len(grid[y]):
                            if grid[y][x+1] == 1:
                                queue.append([y,x+1])
                                grid[y][x+1] = 0
                    
                    max_area = max(max_area,area)
        return max_area