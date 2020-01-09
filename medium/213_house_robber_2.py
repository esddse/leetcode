class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        def line_rob(nums):
            rb, nrb = 0, 0
            for num in nums:
                rb, nrb = nrb+num, max(rb, nrb)
            return max(rb, nrb)
        return max(line_rob(nums[1:]), line_rob(nums[:-1]))