class Solution:
    def colorBorder(self, grid: List[List[int]], r0: int, c0: int, color: int) -> List[List[int]]:
        
        r_size = len(grid)
        c_size = len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def check_border(r, c, r_size, c_size):
            if r == 0 or r == r_size-1 or c == 0 or c == c_size-1:
                return True
            color = grid[r][c]
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if grid[nr][nc] != color:
                    return True
            return False

        borders = []
        checked = [[False for i in range(c_size)] for j in range(r_size)]
        check_color = grid[r0][c0]
        queue = [(r0, c0)]
        while queue:
            new_queue = []
            for r, c in queue:
                checked[r][c] = True
                if check_border(r, c, r_size, c_size):
                    borders.append((r, c))
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if 0<=nr<r_size and 0<=nc<c_size and not checked[nr][nc] and grid[nr][nc] == check_color:
                        new_queue.append((nr, nc))
            queue = new_queue

        for r, c in borders:
            grid[r][c] = color

        return grid

