
import heapq
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
         
        rs = [(w/q, q) for w, q in zip(wage, quality)]
        rs = sorted(rs, key=lambda item: item[0])
        res = float('inf')
        qsum = 0
        heap = []
        for r, q in rs:
            qsum += q
            heapq.heappush(heap, -q)
            if len(heap) > K:
                qsum += heapq.heappop(heap)
            if len(heap) == K:
                res = min(res, qsum * r)
        return res

