import math
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0] * (n+1) for _ in range(n+1)]
        for l in range(2, n+1):
            for i in range(1, n-l+2):
                j = i + l - 1
                min_pay = min(i+dp[i+1][j], dp[i][j-1]+j)
                for k in range(i+1, j):
                    min_pay = min(min_pay, max(k+dp[i][k-1], k+dp[k+1][j]))
                dp[i][j] = min_pay
        return dp[1][n]

        
