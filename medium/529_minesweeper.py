
import copy

class Solution:
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """

        col_len = len(board)
        row_len = len(board[0])
        
        visited = [[False] * row_len for __ in range(col_len)]
        output = copy.deepcopy(board)

        def check_mine(board, col_len, row_len, x, y):
            direction = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
            cnt = 0
            for i in range(8):
                new_x = x + direction[i][0]
                new_y = y + direction[i][1]
                if new_x >= 0 and new_x < col_len and new_y >=0 and new_y < row_len:
                    if board[new_x][new_y] == 'M':
                        cnt += 1
            return cnt

        def recursive_reveal(board, output, visited, col_len, row_len, x, y):
            visited[x][y] = True
            mine_num = check_mine(board, col_len, row_len, x, y)
            if mine_num:
                output[x][y] = str(mine_num)
            else:
                output[x][y] = 'B'
                direction = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
                for i in range(8):
                    new_x = x + direction[i][0]
                    new_y = y + direction[i][1]
                    if new_x >= 0 and new_x < col_len and new_y >=0 and new_y < row_len and board[new_x][new_y] == 'E' and not visited[new_x][new_y]:
                        recursive_reveal(board, output, visited, col_len, row_len, new_x, new_y)

        x, y = click
        if board[x][y] == 'M':
            output[x][y] = 'X'
        elif board[x][y] == 'E':
            recursive_reveal(board, output, visited, col_len, row_len, x, y)
        return output



