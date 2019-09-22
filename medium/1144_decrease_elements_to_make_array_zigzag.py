class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        nums = [float("inf")] + nums + [float("inf")]
        size = len(nums)
        even, odd = 0, 0

        for i in range(1, size-1):
            if i % 2 == 0: # even
                even += max(0, nums[i] - min(nums[i-1], nums[i+1]) + 1)
            else:
                odd += max(0, nums[i] - min(nums[i-1], nums[i+1]) + 1)
        return min(even, odd)