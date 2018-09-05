class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        if len(nums) == 1:
            return [nums]
        permutations = []
        for i in range(len(nums)):
            num = nums[i]
            sub_permutations = self.permute(nums[:i]+nums[i+1:])
            for sub in sub_permutations:
                permutations.append([num] + sub)
        return permutations

