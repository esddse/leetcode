class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x, y, d = 0, 0, 0
        for num in range(1, n * n + 1):
            matrix[x][y] = num
            dx, dy = directions[d]
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= n or matrix[nx][ny] != 0:
                d = (d + 1) % 4
                dx, dy = directions[d]
                nx, ny = x + dx, y + dy
            x, y = nx, ny
        return matrix