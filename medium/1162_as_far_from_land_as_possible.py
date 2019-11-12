class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        col_size = len(grid)
        row_size = len(grid[0])
        dist_mat = [[0 if grid[i][j] else float("inf") for j in range(row_size)] for i in range(col_size)]

        def bfs(x, y):
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            queue = [(x, y)]
            step = 1
            while queue:
                new_queue = []
                for x, y in queue:
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if 0<=nx<col_size and 0<=ny<row_size:
                            if dist_mat[nx][ny] > step:
                                dist_mat[nx][ny] = step
                                new_queue.append((nx, ny))
                queue = new_queue
                step += 1 

        for i in range(col_size):
            for j in range(row_size):
                if grid[i][j]:
                    bfs(i, j)

        max_dist = max([max(row) for row in dist_mat])
        if max_dist == 0 or max_dist == float("inf"):
            return -1 
        return max_dist