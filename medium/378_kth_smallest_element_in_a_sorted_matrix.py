
from heapq import *
class Solution:
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        
        n = len(matrix)
        heap = [(lst[0], i) for i, lst in enumerate(matrix)]
        idxs = [0] * n
        heapify(heap)

        while k:
            val, i = heappop(heap)
            idxs[i] += 1
            if idxs[i] < n:
                heappush(heap, (matrix[i][idxs[i]], i))
            k -= 1
        return val