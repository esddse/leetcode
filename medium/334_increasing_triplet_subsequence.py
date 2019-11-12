import bisect
from collections import defaultdict
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        num_less = defaultdict(bool)
        bst = []
        for num in nums:
            idx = bisect.bisect_left(bst, num)
            if any([num_less[bst[i]] for i in range(idx)]):
                return True 
            else:
                if num not in num_less:
                    bst.insert(idx, num)
                num_less[num] = idx > 0
        return False

            
