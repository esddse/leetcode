from collections import defaultdict
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if not nums:
            return 0
        
        d = defaultdict(int)
        if nums[0] == 0:
            d[0] = 2
        else:
            d[nums[0]]  = 1
            d[-nums[0]] = 1
        
        for num in nums[1:]:
            new_d = defaultdict(int)
            for k, v in d.items():
                new_d[k+num] += v
                new_d[k-num] += v
            d = new_d

        return d[S]
