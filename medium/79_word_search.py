class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0] or not word:
            return False
        row_size = len(board)
        col_size = len(board[0])
        visited = [[False] * col_size for _ in range(row_size)]
        
        def dfs(x, y, word):
            if not word:
                return True
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dx, dy in directions:
                nx, ny = x+dx, y+dy
                if 0<=nx<row_size and 0<=ny<col_size and board[nx][ny] == word[0] and not visited[nx][ny]:
                    visited[nx][ny] = True
                    find = dfs(nx, ny, word[1:])
                    if find:
                        return True
                    visited[nx][ny] = False
            return False

        for x in range(row_size):
            for y in range(col_size):
                if board[x][y] == word[0]:
                    visited[x][y] = True
                    find = dfs(x, y, word[1:])
                    if find:
                        return True 
                    visited[x][y] = False
        return False
