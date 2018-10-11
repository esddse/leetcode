class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        N = len(nums)
        dp = [1] * N

        max_len = 1
        for i in range(1, N):
            if nums[i] > nums[i-1]:
                dp[i] = dp[i-1] + 1
                max_len = max(max_len, dp[i])
        return max_len