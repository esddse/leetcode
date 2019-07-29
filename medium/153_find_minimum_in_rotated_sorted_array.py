class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]
        l, r = 0, len(nums)-1
        if nums[l] < nums[r]:
            return nums[l]
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[l]:
                l = m
            else:
                r = m
        return nums[l+1]