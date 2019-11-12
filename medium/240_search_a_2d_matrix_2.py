class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])

        if m == 1 and n == 1:
            return target == matrix[0][0]
        if target < matrix[0][0]:
            return False
        if target == matrix[0][0]:
            return True
        for i in range(min(m, n)-1):
            if target == matrix[i][i] or target == matrix[i+1][i+1]:
                return True
            if target > matrix[i][i] and target < matrix[i+1][i+1]:
                left_down = [row[:i+1] for row in matrix[i+1:]]
                right_up  = [row[i+1:] for row in matrix[:i+1]]
                if self.searchMatrix(left_down, target) or self.searchMatrix(right_up, target):
                    return True 

        if m == n:
            return False
        elif m > n:
            return self.searchMatrix(matrix[n:], target) 
        else:
            matrix = [row[m:] for row in matrix]
            return self.searchMatrix(matrix, target)