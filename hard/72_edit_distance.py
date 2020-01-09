class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        size1, size2 = len(word1), len(word2)
        dp = [[float("inf")] * (size2+1) for _ in range(size1+1)]
        dp[0][0] = 0
        for i in range(size1):
            dp[i+1][0] = i+1
        for j in range(size2):
            dp[0][j+1] = j+1
        
        for i in range(size1):
            for j in range(size2):
                if word1[i] == word2[j]:
                    dp[i+1][j+1] = min(dp[i][j+1]+1, dp[i+1][j]+1, dp[i][j])
                else:
                    dp[i+1][j+1] = min(dp[i][j+1]+1, dp[i+1][j]+1, dp[i][j]+1)
        return dp[size1][size2]