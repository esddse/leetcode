from collections import Counter
import heapq
class Solution:
    def reorganizeString(self, S: str) -> str:
        size = len(S)
        counter = Counter(S)
        if counter.most_common(1)[0][1] >= size/2+1:
            return ""
        newS = []
        heap = [(-cnt, c) for c, cnt in counter.items()]
        heapq.heapify(heap)
        while len(newS) < size:
            if not newS or heap[0][1] != newS[-1]:
                cnt, c = heapq.heappop(heap)
                newS.append(c)
                heapq.heappush(heap, (cnt+1, c))
            elif heap[0][1] == newS[-1]:
                cnt_1, c_1 = heapq.heappop(heap)
                cnt_2, c_2 = heapq.heappop(heap)
                newS.append(c_2)
                heapq.heappush(heap, (cnt_1, c_1))
                heapq.heappush(heap, (cnt_2+1, c_2))
        return "".join(newS)
