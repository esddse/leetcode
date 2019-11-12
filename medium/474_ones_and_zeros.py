from collections import Counter

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        size = len(strs)
        counters = [0]+[Counter(s) for s in strs]
        dp = [[[0 for i in range(n+1)] for j in range(m+1)] for k in range(size+1)]
        for s in range(1, size+1):
            num0 = counters[s]["0"]
            num1 = counters[s]["1"]
            for i in range(m+1):
                for j in range(n+1):
                    if i < num0 or j < num1:
                        dp[s][i][j] = dp[s-1][i][j]
                    else:
                        dp[s][i][j] = max(dp[s-1][i][j], dp[s-1][i-num0][j-num1]+1)
        return dp[size][m][n] 
