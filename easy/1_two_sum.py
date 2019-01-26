class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        num2idx = {}
        for i, num in enumerate(nums):
            if target - num not in num2idx:
                num2idx[num] = i
            else:
                return [num2idx[target-num], i]