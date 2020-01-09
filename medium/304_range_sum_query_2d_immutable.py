class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            return 
        self.matrix = matrix
        self.row_size = len(matrix)
        self.col_size = len(matrix[0])
        self.down_right_sum = [[0] * self.col_size for _ in range(self.row_size)]
        self.down_right_sum[0][0] = matrix[0][0]  
        for r in range(0, self.row_size):
            for c in range(0, self.col_size):
                if r == 0 and c == 0: 
                    continue
                elif r == 0: 
                    self.down_right_sum[r][c] = self.down_right_sum[r][c-1] + matrix[r][c]
                elif c == 0:
                    self.down_right_sum[r][c] = self.down_right_sum[r-1][c] + matrix[r][c]
                else:
                    self.down_right_sum[r][c] = self.down_right_sum[r-1][c] + self.down_right_sum[r][c-1] - self.down_right_sum[r-1][c-1] + matrix[r][c]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 == 0 and col1 == 0:
            return self.down_right_sum[row2][col2]
        elif row1 == 0:
            return self.down_right_sum[row2][col2] - self.down_right_sum[row2][col1-1]
        elif col1 == 0:
            return self.down_right_sum[row2][col2] - self.down_right_sum[row1-1][col2]
        else:
            return self.down_right_sum[row2][col2] - self.down_right_sum[row2][col1-1] - self.down_right_sum[row1-1][col2] + self.down_right_sum[row1-1][col1-1]
