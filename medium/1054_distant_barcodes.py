from collections import Counter, deque
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        size = len(barcodes)
        counter = Counter(barcodes)
        rets = [0] * size 
        lst = []
        for num, cnt in counter.most_common():
            lst += [num] * cnt
        lst = deque(lst)
        # even
        for i in range(0, size, 2):
            rets[i] = lst.popleft()
        for i in range(1, size, 2):
            rets[i] = lst.popleft()
        return rets