
import math
class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """

        col_len = len(M)
        row_len = len(M[0])

        def smooth(M, x, y, col_len, row_len):
            cnt, s = 0, 0
            directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if nx >= 0 and nx < col_len and ny >=0 and ny < row_len:
                    s += M[nx][ny]
                    cnt += 1
            return math.floor(s / cnt)

        SM = [[0] * row_len for _ in range(col_len)]
        for i in range(col_len):
            for j in range(row_len):
                SM[i][j] = smooth(M, i, j, col_len, row_len)
        return SM

        