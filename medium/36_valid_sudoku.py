class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def check_unit_valid(unit):
            return len(set(unit)) == len(unit)

        def check_row_valid():
            ret = True
            for row in board:
                row = [item for item in row if item != "."]
                ret &= check_unit_valid(row)
            return ret

        def check_col_valid():
            ret = True
            for col in zip(*board):
                col = [item for item in col if item != "."]
                ret &= check_unit_valid(col)
            return ret

        def check_box_valid():
            ret = True
            for i in [0, 3, 6]:
                for j in [0, 3, 6]:
                    box = board[i][j:j+3] + board[i+1][j:j+3] + board[i+2][j:j+3]
                    box = [item for item in box if item != "."]
                    ret &= check_unit_valid(box)
            return ret

        return check_row_valid() & check_col_valid() & check_box_valid()