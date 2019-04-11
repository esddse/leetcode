class Solution:
    def numTrees(self, n: int) -> int:
        dp = [1] * (n+1)
        for i in range(2, n+1):
            cnt = 0
            for l in range(i):
                r = i - l - 1
                cnt += (dp[l] * dp[r]) 
            dp[i] = cnt
        return dp[n]