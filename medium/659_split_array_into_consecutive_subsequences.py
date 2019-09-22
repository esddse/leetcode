import heapq
from collections import defaultdict
class Solution:
    def isPossible(self, nums: List[int]) -> bool:

        seq_lengths = defaultdict(list)
        for num in nums:
            if seq_lengths[num-1]:
                min_len = heapq.heappop(seq_lengths[num-1])
                heapq.heappush(seq_lengths[num], min_len+1)
            else:
                heapq.heappush(seq_lengths[num], 1)

        for _, lengths in seq_lengths.items():
            for l in lengths:
                if l < 3:
                    return False
        return True