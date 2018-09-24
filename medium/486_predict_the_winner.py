class Solution:
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        size = len(nums)
        
        dp = [[0] * size for _ in nums]
        for i in range(size):
            dp[i][i] = nums[i]
        for l in range(1, size):
            for i in range(0, size - l):
                j = i + l
                dp[i][j] = max(nums[i] - dp[i+1][j], nums[j] - dp[i][j-1])
        return dp[0][size-1] >= 0