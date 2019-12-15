class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        row_size, col_size = len(matrix), len(matrix[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        ret = [matrix[0][0]]
        matrix[0][0] = "#"
        x, y, d = 0, 0, 0
        for _ in range(row_size*col_size-1):
            dx, dy = directions[d]
            nx, ny = x+dx, y+dy
            if nx < 0 or nx >= row_size or ny < 0 or ny >= col_size or matrix[nx][ny] == "#":
                d = (d+1)%4
                dx, dy = directions[d]
                nx, ny = x+dx, y+dy
            x, y = nx, ny
            ret.append(matrix[x][y])
            matrix[x][y] = "#"
        return ret
