import heapq
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1
        heap = [1]
        checked = {1}
        cnt = 1
        for _ in range(1, n):
            smallest = heapq.heappop(heap)
            for plus in [2,3,5]:
                num = smallest * plus 
                if num not in checked:
                    heapq.heappush(heap, num)
                    checked.add(num)
        return heapq.heappop(heap) 
