import bisect
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        row_size = len(matrix)
        col_size = len(matrix[0])

        array = []
        for row in matrix:
            array += row

        idx = bisect.bisect_left(array, target)

        if idx >= row_size * col_size or target != array[idx]:
            return False
        return True
