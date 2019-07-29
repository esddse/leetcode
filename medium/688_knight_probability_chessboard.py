from collections import defaultdict

class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        d = [(-2, -1), (-1, -2), (-2, 1), (-1, 2), (2, -1), (1, -2), (2, 1), (1, 2)]
        possible_next = {}
        rawr, rawc = r, c
        for r in range(N):
            for c in range(N):
                possible_next[r, c] = []
                for dr, dc in d:
                    nr, nc = r+dr, c+dc
                    if (nr >= 0 and nr < N) and (nc >= 0 and nc < N):
                        possible_next[r, c].append((nr, nc))

        queue = {(rawr, rawc): 1}
        while queue and K:
            new_queue = defaultdict(float)
            for rc, p in queue.items():
                r, c = rc
                for nr, nc in possible_next[r, c]:
                    new_queue[nr, nc] += p * 0.125
            queue = new_queue
            K -= 1

        if not queue:
            return 0
        else:
            return sum([v for k, v in queue.items()])


        

