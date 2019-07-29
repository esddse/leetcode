class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        size = len(A)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]


        def first():
            for i in range(size):
                for j in range(size):
                    if A[i][j]:
                        return i, j

        queue = []
        def dfs(x, y):
            queue.append((x,y))
            A[x][y] = 2
            for dx, dy in directions:
                nx, ny = x+dx, y+dy
                if 0 <= nx < size and 0 <= ny < size and A[nx][ny] == 1:
                    dfs(nx, ny)

        x, y = first()
        dfs(x, y)

        step = 0
        while queue:
            new_queue = []
            for x, y in queue:
                for dx, dy in directions:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < size and 0 <= ny < size:
                        if A[nx][ny] == 1:
                            return step 
                        elif A[nx][ny] == 0:
                            new_queue.append((nx, ny))
                            A[nx][ny] = 2

            step += 1
            queue = new_queue
