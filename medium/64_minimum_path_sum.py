class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        row_size = len(grid)
        col_size = len(grid[0])
        dp = [[0] * col_size for _ in range(row_size)]
        dp[0][0] = grid[0][0]
        for j in range(1, col_size):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        for i in range(1, row_size):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for i in range(1, row_size):
            for j in range(1, col_size):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[row_size-1][col_size-1]
