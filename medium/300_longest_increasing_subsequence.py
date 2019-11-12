class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [1] * len(nums)
        for i, num in enumerate(nums):
            for j in range(i):
                if nums[j] < num:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)