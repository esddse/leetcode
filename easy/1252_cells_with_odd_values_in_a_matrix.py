from collections import Counter
class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        rows, cols = zip(*indices)
        cnt_rows, cnt_cols = Counter(rows), Counter(cols)
        row_num = len([k for k, v in cnt_rows.items() if v % 2 == 1])
        col_num = len([k for k, v in cnt_cols.items() if v % 2 == 1])
        return row_num * m + col_num * n - 2 *row_num * col_num
