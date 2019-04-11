class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        size = len(A)
        v2id = {v: i for i, v in enumerate(A)}
        dp = [[0] * size for _ in range(size)]
        max_len = 2
        for i in range(0, size):
            for j in range(i+1, size):
                d = A[j] - A[i]
                dp[i][j] = dp[v2id[d]][i] + 1 if d in v2id and d < A[i] else 2
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
        return max_len if max_len > 2 else 0