class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        size = len(stones)
        total  = sum(stones)
        target = total // 2
        dp = [[0] * (target+1) for _ in range(size)]
        for i in range(size):
            for t in range(target+1):
                if t < stones[i]:
                    dp[i][t] = dp[i-1][t]
                else:
                    dp[i][t] = max(dp[i-1][t], dp[i-1][t-stones[i]]+stones[i])
        return total-2*dp[size-1][target]