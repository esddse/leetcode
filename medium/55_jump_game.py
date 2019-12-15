class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False
        size = len(nums)
        for i in range(size):
            nums[i] += i
        start, end = 0, 0
        while start <= end:
            if end >= size-1:
                return True
            max_end = 0
            for i in range(start, end+1):
                max_end = max(nums[i], max_end)
            start, end = end+1, max_end
        return False
