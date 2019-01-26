
from collections import defaultdict
class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        
        cost = {i:float("inf") for i in range(1, N+1)}
        u2v = defaultdict(list)

        for u, v, w in times:
            u2v[u].append((v, w))

        queue = [(K, 0)]
        while queue:
            new_queue = []
            for u, c in queue:
                cost[u] = c 
                for v, w in u2v[u]:
                    if c + w < cost[v]:
                        new_queue.append((v, c+w))
            queue = new_queue

        cost = max(cost.values())
        if cost == float("inf"):
            return -1
        else:
            return cost
