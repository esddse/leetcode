class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        len_A, len_B = len(A), len(B)
        dp = [[0] * len_B for _ in range(len_A)]
        for i in range(len_A):
            if A[i] == B[0]:
                dp[i][0] = 1
        for j in range(len_B):
            if A[0] == B[j]:
                dp[0][j] = 1
        ret = 0
        for i in range(1, len_A):
            for j in range(1, len_B):
                dp[i][j] = dp[i-1][j-1]+1 if A[i] == B[j] else 0
                ret = max(ret, dp[i][j])
        return ret