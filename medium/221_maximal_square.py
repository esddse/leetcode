class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        row_size, col_size = len(matrix), len(matrix[0])
    
        dp_row = [[0] * col_size for _ in range(row_size)]
        for r in range(row_size):
            dp_row[r][0] = int(matrix[r][0])
        for r in range(row_size):
            for c in range(1, col_size):
                dp_row[r][c] = dp_row[r][c-1] + 1 if matrix[r][c] == "1" else 0
                
        dp_col = [[0] * col_size for _ in range(row_size)]
        for c in range(col_size):
            dp_col[0][c] = int(matrix[0][c])
        for r in range(1, row_size):
            for c in range(col_size):
                dp_col[r][c] = dp_col[r-1][c] + 1 if matrix[r][c] == "1" else 0
        
        max_d = 0
        dp = [[int(matrix[i][j]) for j in range(col_size)] for i in range(row_size)]
        for r in range(row_size):
            for c in range(col_size):
                if r == 0 or c == 0:
                    max_d = max(max_d, dp[r][c])
                else:
                    dp[r][c] = min(dp[r-1][c-1], dp_row[r][c-1], dp_col[r-1][c]) + 1 if dp[r][c] else 0
                    max_d = max(max_d, dp[r][c])
        return max_d ** 2