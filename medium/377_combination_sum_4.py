from collections import defaultdict

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        dp = [1] + [0] * target
        for t in range(target+1):
            for i, num in enumerate(nums):
                if num >  t: continue
                if num == t: dp[t] += 1
                if num <  t: dp[t] += dp[t-num]
        return dp[target]