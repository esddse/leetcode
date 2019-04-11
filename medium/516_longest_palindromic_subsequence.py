class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if not s:
            return 0
        length = len(s)
        dp = [[0] * length for _ in range(length)]
        for i in range(length):
            dp[i][i] = 1
        for l in range(2, length+1):
            for start in range(length-l+1):
                end = start + l - 1
                if s[start] == s[end]:
                    if start+1 > end-1:
                        dp[start][end] = 2
                    else:
                        dp[start][end] = dp[start+1][end-1] + 2 if dp[start+1][end-1] > 0 else 0
                else:
                    dp[start][end] = max(dp[start][end-1], dp[start+1][end])
        return dp[0][length-1]