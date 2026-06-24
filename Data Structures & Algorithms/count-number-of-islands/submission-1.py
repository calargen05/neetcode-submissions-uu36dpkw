'''
    UPI Method:
        U - Understand: The problem is asking for me to find the number of islands in the grid,
        indicated by the number of groups of 1's (touching vertically or horizontally)
        P - Plan: I plan on iterating through the grid, finding a 1 and checking which direction
        to go, finding all of the 1's in the island, keeping track of their positions with a set,
        and setting all of the found 1's to 0 after i counted the groups of 1's as an island
        I - Implement: see below VVV
'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        queue = deque()
        islands = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    # implement bfs
                    queue.append([i,j])
                    grid[i][j] = '0'
                    while queue:
                        point = queue.popleft()
                        y,x = point[0], point[1]
                        # check up
                        if y-1 >= 0:
                            if grid[y-1][x] == '1':
                                queue.append([y-1,x])
                                grid[y-1][x] = '0'
                        # check left
                        if x-1 >= 0:
                            if grid[y][x-1] == '1':
                                queue.append([y,x-1])
                                grid[y][x-1] = '0'
                        # check down
                        if y+1 < len(grid):
                            if grid[y+1][x] == '1':
                                queue.append([y+1,x])
                                grid[y+1][x] = '0'
                        # check right
                        if x+1 < len(grid[y]):
                            if grid[y][x+1] == '1':
                                queue.append([y,x+1])
                                grid[y][x+1] = '0'
                    islands += 1
        return islands
