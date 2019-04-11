class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        min_num = nums[-1]
        a = -1
        for i in range(len(nums)-1, -1, -1):
            if min_num > nums[i]:
                min_num = nums[i]
            if nums[i] > min_num:
                a = i

        max_num = nums[0]
        b = -1
        for i in range(len(nums)):
            if max_num < nums[i]:
                max_num = nums[i]
            if nums[i] < max_num:
                b = i 

        if a < 0:
            return 0
        return b-a+1

