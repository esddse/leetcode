class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r, m = 0, len(nums)-1, 0
        while l <= m <= r:
            if nums[m] == 0:
                nums[l], nums[m] = nums[m], nums[l]
                while l <= r and nums[l] == 0:
                    l += 1
                m = max(m, l)
            elif nums[m] == 2:
                nums[r], nums[m] = nums[m], nums[r]
                while l <= r and nums[r] == 2:
                    r -= 1
            else:
                m += 1
