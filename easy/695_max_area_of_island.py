class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        def check(grid, checked, i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or checked[i][j]:
                return 0
            checked[i][j] = True
            if not grid[i][j]:
                return 0
            return 1 + \
                   check(grid, checked, i+1, j) + \
                   check(grid, checked, i-1, j) + \
                   check(grid, checked, i, j+1) + \
                   check(grid, checked, i, j-1)


        checked = [[False] * len(grid[0]) for __ in grid]
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not checked[i][j]:
                    area = check(grid, checked, i, j)
                    if area > max_area:
                        max_area = area
        return max_area