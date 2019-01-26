
from heapq import *
class KthLargest:

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        
        self.k = k
        self.top_k_heap = nums

        heapify(self.top_k_heap)
        while len(self.top_k_heap) > k: 
            heappop(self.top_k_heap)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        
        if len(self.top_k_heap) < self.k:
            heappush(self.top_k_heap, val)
        elif val > self.top_k_heap[0]:
            heapreplace(self.top_k_heap, val)
        return self.top_k_heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)