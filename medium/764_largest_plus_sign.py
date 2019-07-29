class Solution:
    def orderOfLargestPlusSign(self, N: int, mines: List[List[int]]) -> int:
        if len(mines) == N ** 2:
            return 0

        mines = {(i, j) for i, j in mines}
        mat = [[[0, 0, 0, 0] for b in range(N)] for a in range(N)] # 左右上下

        for i in range(N):
            cnt_row, cnt_col = 0, 0
            for j in range(N):
                # row
                if (i, j) in mines:
                    for k in range(cnt_row):
                        mat[i][j-cnt_row+k][0] = k
                        mat[i][j-cnt_row+k][1] = cnt_row-k-1
                    cnt_row = 0
                else:
                    cnt_row += 1
                # col
                if (j, i) in mines:
                    for k in range(cnt_col):
                        mat[j-cnt_col+k][i][2] = k
                        mat[j-cnt_col+k][i][3] = cnt_col-k-1
                    cnt_col = 0
                else:
                    cnt_col += 1

            # row
            for k in range(cnt_row):
                # print(i, j-cnt_row+k+1, k)
                mat[i][j-cnt_row+k+1][0] = k
                mat[i][j-cnt_row+k+1][1] = cnt_row-k-1
            for k in range(cnt_col):
                mat[j-cnt_col+k+1][i][2] = k
                mat[j-cnt_col+k+1][i][3] = cnt_col-k-1


        order = max([min(nums) for row in mat for nums in row]) + 1
        return order
                
