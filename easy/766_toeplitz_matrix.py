class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        col_len = len(matrix)
        row_len = len(matrix[0])

        def check(start_i, start_j, col_len, row_len, matrix):
            num = matrix[start_i][start_j]
            i = start_i + 1
            j = start_j + 1
            while i < col_len and j < row_len:
                if matrix[i][j] != num:
                    return False
                i += 1
                j += 1
            return True

        for i in range(col_len):
            if not check(i, 0, col_len, row_len, matrix):
                return False
        for j in range(1, row_len):
            if not check(0, j, col_len, row_len, matrix):
                return False
        return True
