class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        r_size = len(grid)
        c_size = len(grid[0])

        def check_valid(r, c, length):
            for i in range(length):
                if grid[r+i][c] != 1 or grid[r][c+i] != 1 or grid[r+length-1][c+i] != 1 or grid[r+i][c+length-1] != 1:
                    return False
            return True

        for length in range(min(r_size, c_size), 0, -1):
            for r in range(r_size):
                for c in range(c_size):
                    if 0<=r+length-1<r_size and 0<=c+length-1<c_size and grid[r][c]:
                        if check_valid(r, c, length):
                            return length * length
        return 0

