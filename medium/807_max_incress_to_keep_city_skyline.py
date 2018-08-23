class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        import numpy as np
        grid_np = np.array(grid)

        col_skyline = np.max(grid_np, axis=0)
        row_skyline = np.max(grid_np, axis=1)

        s = 0
        for i in range(len(grid)):
        	for j in range(len(grid[i])):
        		upper_bound = min(col_skyline[j], row_skyline[i])
        		s += int(upper_bound) - grid[i][j]
        return s
