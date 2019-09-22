
import random
import bisect
class Solution:

    def __init__(self, w: List[int]):
        start = 0
        self.arr = []
        for weight in w:
            self.arr.append(start)
            start += weight
        self.size = start


    def pickIndex(self) -> int:
        num = random.randint(0, self.size-1)
        i = bisect.bisect_right(self.arr, num)
        return i-1


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()