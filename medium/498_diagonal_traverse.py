class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        M = len(matrix)
        if M == 0:
            return []
        N = len(matrix[0])
        if N == 0:
            return []
        directions = [[-1, 1], [1, -1]]
        x, y = 0, 0
        d = 0
        ret = []
        while (x, y) != (M-1, N-1):
            print(x, y)
            ret.append(matrix[x][y])
            dx, dy = directions[d]
            nx, ny = x + dx, y + dy
            if nx < 0 and ny >= N:
                nx = 1
                ny = N-1
                d = (d+1)%2
            elif nx >= M and ny < 0:
                nx = M-1
                ny = 1
                d = (d+1)%2
            elif nx < 0:
                nx = 0
                d = (d+1)%2
            elif nx >= M:
                nx = M-1
                ny += 2
                d = (d+1)%2
            elif ny < 0:
                ny = 0
                d = (d+1)%2
            elif ny >= N:
                nx += 2
                ny = N-1
                d = (d+1)%2
            x, y = nx, ny
        ret.append(matrix[x][y])
        return ret