from collections import Counter
class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        if upper + lower != sum(colsum):
            return []
        col_counter = Counter(colsum)
        cnt_2 = col_counter[2]
        if upper < cnt_2 or lower < cnt_2:
            return []
        row1, row2 = [], []
        for col in colsum:
            if col == 2:
                row1.append(1)
                row2.append(1)
                upper -= 1
                lower -= 1
            elif col == 1:
                if upper > lower:
                    row1.append(1)
                    row2.append(0)
                    upper -= 1
                else:
                    row1.append(0)
                    row2.append(1)
                    lower -= 1
            else:
                row1.append(0)
                row2.append(0)
        return [row1, row2]

