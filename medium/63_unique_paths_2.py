class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        if not obstacleGrid or not obstacleGrid[0]:
            return 0
        row_size = len(obstacleGrid)
        col_size = len(obstacleGrid[0])
        dp = [[0] * col_size for _ in range(row_size)]
        dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
        for i in range(row_size):
            for j in range(col_size):
                if obstacleGrid[i][j] == 1:
                    continue
                if 0<=i-1<row_size and obstacleGrid[i-1][j] == 0:
                    dp[i][j] += dp[i-1][j]
                if 0<=j-1<col_size and obstacleGrid[i][j-1] == 0:
                    dp[i][j] += dp[i][j-1]
        return dp[row_size-1][col_size-1]