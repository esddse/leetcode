class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        size = len(graph)
        part = [None] * size

        def bfs(idx):
            queue = [idx]
            tag = 1
            while queue:
                new_queue = []
                for idx in queue:
                    if not part[idx]:
                        part[idx] = tag
                        new_queue += graph[idx]
                    else:
                        if tag != part[idx]:
                            return False
                queue = new_queue
                tag *= -1
            return True

        for idx in range(size):
            if not part[idx]:
                if not bfs(idx):
                    return False 
        return True