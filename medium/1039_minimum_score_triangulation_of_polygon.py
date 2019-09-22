class Solution:
    def minScoreTriangulation(self, A: List[int]) -> int:
        size = len(A)
        dp = [[0] * size for _ in range(size)]

        for l in range(3, size+1):
            for s in range(0, size-l+1):
                e = s+l-1
                dp[s][e] = min(dp[s][k]+dp[k][e]+A[s]*A[k]*A[e] for k in range(s+1, e))
        return dp[0][size-1]