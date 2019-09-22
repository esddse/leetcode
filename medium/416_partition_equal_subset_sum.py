class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        size = len(nums)
        sum_nums = sum(nums)
        if sum_nums % 2 != 0:
            return False
        target = sum_nums // 2

        dp = [True] + [False] * target
        for i, num in enumerate(nums):
            if num > target:
                return False
            for i in range(target, num-1, -1):
                dp[i] = dp[i] or dp[i-num]

        return dp[target]