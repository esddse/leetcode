class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        checks = [False] * (len(nums)+1)
        for num in nums:
            checks[num] = True
        for i, check in enumerate(checks):
            if not check:
                return i