import copy
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
            return []

        row_size = len(matrix)
        col_size = len(matrix[0])

        pacific_init = set([(i, 0) for i in range(row_size)] + [(0, i) for i in range(col_size)])
        atlantic_init = set([(i, col_size-1) for i in range(row_size)] + [(row_size-1, i) for i in range(col_size)])

        def bfs(nodes):
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            queue = copy.deepcopy(nodes)
            while queue:
                next_queue = set()
                for x, y in queue:
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if 0<=nx<row_size and 0<=ny<col_size and (nx, ny) not in nodes and matrix[nx][ny] >= matrix[x][y]:
                            nodes.add((nx, ny))
                            next_queue.add((nx, ny))
                queue = next_queue
            return nodes

        return bfs(pacific_init) & bfs(atlantic_init)



