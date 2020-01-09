from collections import Counter
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        size = len(nums)
        if size == 0 or size % k != 0:
            return False
        counter = Counter(nums)
        for i in sorted(counter):
            if counter[i] == 0:
                continue 
            elif counter[i] < 0 or counter[i] > size // k:
                return False 
            else:
                cnt = counter[i]
                for j in range(i, i+k):
                    if j not in counter:
                        return False 
                    else:
                        counter[j] -= cnt 
        return True