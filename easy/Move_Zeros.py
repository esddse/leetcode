class Solution(object):
    def exchange(self, nums, index1, index2):
        temp = nums[index1]
        nums[index1] = nums[index2]
        nums[index2] = temp
        
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero_index = 0
        while zero_index < len(nums) and nums[zero_index] != 0:
            zero_index += 1
        p = zero_index + 1
        
        while p < len(nums):
            if nums[p] != 0:
                self.exchange(nums, zero_index, p)
                zero_index += 1
            p += 1