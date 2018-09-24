
from collections import defaultdict
class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num2freq  = defaultdict(int)
        freq2num  = defaultdict(list)
        num2start = dict()
        num2end   = dict()
        max_freq  = 0

        for i in range(len(nums)):
            num = nums[i]
            if num not in num2start:
                num2start[num] = i
            num2end[num] = i
            num2freq[num] += 1
            max_freq = max(max_freq, num2freq[num])
            freq2num[num2freq[num]].append(num)

        return min([num2end[num] - num2start[num] + 1 for num in freq2num[max_freq]])
        
