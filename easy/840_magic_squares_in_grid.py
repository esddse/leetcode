class Solution:
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        def check_magic(i, j):
            num = 1^2^3^4^5^6^7^8^9
            for n in range(i, i+3):
                for m in range(j, j+3):
                    num ^= grid[n][m]
            if num:
                return False
            s = sum(grid[i][j:j+3])
            for k in range(i+1, i+3):
                if sum(grid[k][j:j+3]) != s:
                    return False
            for k in range(j, j+3):
                if sum([grid[i][k], grid[i+1][k], grid[i+2][k]]) != s:
                    return False
            if sum([grid[i][j], grid[i+1][j+1], grid[i+2][j+2]]) != s:
                return False
            if sum([grid[i][j+2], grid[i+1][j+1], grid[i+2][j]]) != s:
                return False
            return True

        row_size = len(grid)
        col_size = len(grid[0])
        if row_size < 3 or col_size < 3:
            return 0
        
        cnt = 0
        for row in range(row_size-2):
            for col in range(col_size-2):
                if check_magic(row, col):
                    cnt += 1
        return cnt
