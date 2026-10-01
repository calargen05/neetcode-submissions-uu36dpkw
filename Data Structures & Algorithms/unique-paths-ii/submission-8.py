class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[-1][-1] == 1 or obstacleGrid[0][0] == 1:
            return 0

        n, m = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0]*m for _ in range(n)]

        # get the top and left edge of the paths matrix filled in
        for i in range(m):
            if obstacleGrid[0][i] == 1:
                break
            dp[0][i] = 1
        
        for i in range(n):
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1
        
        for i in range(1,n):
            for j in range(1,m):
                top, left = dp[i-1][j], dp[i][j-1]
                if obstacleGrid[i-1][j] == 1:
                    top = 0
                if obstacleGrid[i][j-1] == 1:
                    left = 0
                dp[i][j] = top + left
        
        return dp[-1][-1]