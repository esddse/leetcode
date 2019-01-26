import heapq
from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        num2idx = defaultdict(list)
        for i, num in enumerate(nums):
            heapq.heappush(num2idx[num], i)
        for _, lst in num2idx.items():
            last_i = lst[0]
            for i in lst[1:]:
                if abs(i - last_i) <= k:
                    return True
                last_i = i 
        return False
