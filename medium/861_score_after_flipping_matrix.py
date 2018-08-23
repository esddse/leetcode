class Solution:

    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """

        col_len = len(A)
        row_len = len(A[0])

        def flip_row(row):
            return [1 if num == 0 else 0 for num in row]

        for i in range(col_len):
            if A[i][0] == 0:
                A[i] = flip_row(A[i])

        num = 0
        for i in range(row_len-1, -1, -1):
            cnt0, cnt1 = 0, 0
            for j in range(col_len):
                if A[j][i] == 1:
                    cnt1 += 1
                else:
                    cnt0 += 1
            num += max(cnt0, cnt1) * pow(2, row_len-i-1)
        return num

