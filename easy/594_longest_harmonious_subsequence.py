
from collections import Counter
class Solution:
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        counter = Counter(nums)
        ans = 0
        for num in counter:
            if num in counter:
                if num+1 in counter:
                    ans = max(ans, counter[num] + counter[num+1])
        return ans