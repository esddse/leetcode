class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        s = "#" + s
        size = len(s)
        dp = [1] * size
        for i in range(1, size):
            if s[i] == "0":
                if s[i-1] == "1" or s[i-1] == "2":
                    dp[i] = dp[i-2]
                else:
                    return 0
            elif int(s[i]) <= 6:
                if s[i-1] == "1" or s[i-1] == "2":
                    dp[i] = dp[i-1] + dp[i-2]
                else:
                    dp[i] = dp[i-1]
            else:
                if s[i-1] == "1":
                    dp[i] = dp[i-1] + dp[i-2]
                else:
                    dp[i] = dp[i-1]
        return dp[size-1]