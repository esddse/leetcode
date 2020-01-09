class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = [0] + nums
        size = len(nums)
        for i in range(size):
            # valid num
            if 0 <= nums[i] < size:
                num = nums[i]
                if num == i:
                    continue
                while 0 <= num < size and nums[num] != num:
                    nums[i], nums[num] = nums[num], nums[i]
                    num = nums[i]
                if num != i:
                    nums[i] = -1
            # invalid num
            else:
                nums[i] = -1
        for i, num in enumerate(nums):
            if num == -1:
                return i 
        return size