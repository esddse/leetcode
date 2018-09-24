class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums.sort()
        for i, j in zip(nums, nums[1:]):
            if i == j:
                return i
        return -1