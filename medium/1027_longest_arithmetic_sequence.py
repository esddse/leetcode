class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:

        dps = [{},{A[1]-A[0]:2}]
        max_len = 0
        for i in range(2, len(A)):
            dp = {}
            for j in range(i):
                diff = A[i] - A[j]
                if diff in dps[j]:
                    dp[diff] = dps[j][diff] + 1
                else:
                    dp[diff] = 2
            max_len = max([max_len] + list(dp.values()))
            # print(i, max_len, dp)
            dps.append(dp)

        return max_len