from heapq import *
class Solution:
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        N = len(grid)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        heap = [(grid[0][0], (0, 0))] # (time, (x, y)) 
        mark = [[float("inf")] * N for _ in range(N)]
        mark[0][0] = grid[0][0]

        while heap:
            t, xy = heappop(heap)
            x, y = xy
            if x == N-1 and y == N-1:
                return t
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if nx >= 0 and nx < N and ny >= 0 and ny < N:
                    nt = max(t, grid[nx][ny])
                    if nt < mark[nx][ny]:
                        mark[nx][ny] = nt
                        item = (nt, (nx, ny))
                        heappush(heap, item)
