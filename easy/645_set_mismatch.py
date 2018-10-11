class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        counter = [0] * (len(nums) + 1)
        for num in nums:
            counter[num] += 1
        for i in range(1, len(nums)+1):
            if counter[i] == 2:
                dup = i 
            elif counter[i] == 0:
                missing = i 
        return [dup, missing]
