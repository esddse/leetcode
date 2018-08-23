class Solution:
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        def str2ascii(string):
            return [ord(c) for c in string]
        
        ascii1 = str2ascii(s1)
        ascii2 = str2ascii(s2)

        dp = [[0] * (len(s2)+1) for _ in range(len(s1)+1)]
        for i in range(len(s1)):
            for j in range(len(s2)):
                if ascii1[i] == ascii2[j]:
                    dp[i+1][j+1] = dp[i][j] + 2 * ascii1[i]
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

        return sum(ascii1) + sum(ascii2) - dp[i+1][j+1]


