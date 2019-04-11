class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        len_row = len(grid)
        if not len_row:
            return 0
        len_col = len(grid[0])

        queue = []
        cnt_f = 0
        for x in range(len_row):
            for y in range(len_col):
                if grid[x][y] == 2:
                    queue.append((x,y))
                elif grid[x][y] == 1:
                    cnt_f += 1
        if cnt_f == 0:
            return 0

        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        cnt_min = 0
        while queue:
            new_queue = []
            for x, y in queue:
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or nx >= len_row or ny < 0 or ny >= len_col:
                        continue
                    if grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        new_queue.append((nx, ny))
                        cnt_f -= 1
            queue = new_queue
            cnt_min += 1
            if not cnt_f:
                return cnt_min
        return -1
