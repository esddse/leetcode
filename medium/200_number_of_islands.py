class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        size_row = len(grid)
        size_col = len(grid[0])
        checked = [[False] * size_col for _ in range(size_row)]

        def dye_island(x, y):
            directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
            queue = [(x, y)]
            checked[x][y] = True
            while queue:
                new_queue = []
                for x, y in queue:
                    grid[x][y] = "*"
                    for dx, dy in directions:
                        nx, ny = x+dx, y+dy
                        if 0<=nx<size_row and 0<=ny<size_col and grid[nx][ny] == "1" and not checked[nx][ny]:
                            new_queue.append((nx, ny))
                            checked[nx][ny] = True
                queue = new_queue

        cnt = 0
        for i in range(size_row):
            for j in range(size_col):
                if grid[i][j] == "1":
                    cnt += 1
                    dye_island(i, j)

        return cnt