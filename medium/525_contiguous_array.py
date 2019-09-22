class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        size = len(nums)
        sum_start = {0:-1}
        res = 0
        s = 0
        for i, num in enumerate(nums):
            if num == 0:
                s += -1
            else:
                s += 1
            if s in sum_start:
                res = max(i-sum_start[s], res)
            else:
                sum_start[s] = i
        return res