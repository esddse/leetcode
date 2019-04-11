from collections import Counter
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0
        counter, prev, curr = Counter(nums), 0, 0
        for num in range(max(nums)+1):
            prev, curr = curr, max(prev + num * counter[num], curr)
        return curr

