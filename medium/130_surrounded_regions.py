class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        if not board or not board[0]:
            return
        row_size = len(board)
        col_size = len(board[0])
        
        def bfs(x, y):
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            board[x][y] = 1
            queue = [(x, y)]
            while queue:
                new_queue = []
                for x, y in queue:
                    for dx, dy in directions:
                        nx, ny = x+dx, y+dy
                        if 0<=nx<row_size and 0<=ny<col_size and board[nx][ny] == "O":
                            board[nx][ny] = 1
                            new_queue.append((nx, ny))
                queue = new_queue
        
        for r in range(row_size):
            if board[r][0] == "O":
                bfs(r, 0)
            if board[r][col_size-1] == "O":
                bfs(r, col_size-1)
        
        for c in range(col_size):
            if board[0][c] == "O":
                bfs(0, c)
            if board[row_size-1][c] == "O":
                bfs(row_size-1, c)
                
        for i in range(row_size):
            for j in range(col_size):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == 1:
                    board[i][j] = "O"
        