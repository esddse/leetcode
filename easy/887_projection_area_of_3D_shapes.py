class Solution:
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        a_top = sum([grid[i][j] != 0 for i in range(len(grid)) for j in range(len(grid[0]))])
        a_row = sum([max(row) for row in grid])
        a_col = [0] * len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > a_col[j]:
                    a_col[j] = grid[i][j]
        a_col = sum(a_col)

        print(a_top, a_row, a_col)

        return a_top + a_row + a_col         