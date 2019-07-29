class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or len(board) == 0 or board[0] == 0:
            return

        x_size = len(board)
        y_size = len(board[0])


        def countN(x, y):
            cnt = 0
            ds = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
            for dx, dy in ds:
                nx, ny = x+dx, y+dy
                if nx >= 0 and nx < x_size and ny >= 0 and ny < y_size:
                    if board[nx][ny] == 1 or board[nx][ny] == 3:
                        cnt += 1
            return cnt

        for x in range(x_size):
            for y in range(y_size):
                cnt = countN(x, y)
                if board[x][y] == 1:
                    if cnt < 2 or cnt > 3:
                        board[x][y] = 3
                else:
                    if cnt == 3:
                        board[x][y] = 2

        for x in range(x_size):
            for y in range(y_size):
                if board[x][y] == 2:
                    board[x][y] = 1
                elif board[x][y] == 3:
                    board[x][y] = 0