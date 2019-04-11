class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        length = len(A)
        if length == 1:
            return 1
        B = []
        for i in range(length-1):
            sign = A[i+1] - A[i]
            if sign > 0:
                sign = 1
            elif sign < 0:
                sign = -1
            B.append(sign)
        
        dp = [0] * (length-1)
        dp[0] = 1 if B[0] != 0 else 0
        for i in range(1, length-1):
            if B[i] == 0:
                dp[i] = 0
            else:
                dp[i] = dp[i-1] + 1 if B[i] == -B[i-1] else 1
        return max(dp) + 1


