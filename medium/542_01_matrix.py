class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        row_size = len(matrix)
        col_size = len(matrix[0])

        dist = [[None] * col_size for _ in range(row_size)]

        queue = []
        for r in range(row_size):
            for c in range(col_size):
                if matrix[r][c] == 0:
                    dist[r][c] = 0
                    queue.append((r, c, 0))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # bfs
        while queue:
            new_queue = []
            for r, c, d in queue:
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if 0<=nr<row_size and 0<=nc<col_size and dist[nr][nc] is None:
                        dist[nr][nc] = d + 1
                        new_queue.append((nr, nc, d+1))
            queue = new_queue
        return dist
