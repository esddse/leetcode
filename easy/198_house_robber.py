class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [num for num in nums]
        for i in range(2, len(nums)):
            dp[i] += max(dp[:i-1])
        return max(dp)

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev, curr = 0, 0
        for num in nums:
            prev, curr = curr, max(prev + num, curr)
        return curr

