class Solution(object):
    def largestOverlap(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """
        N = len(A)
        LA = [i // N * 100 + i % N for i in range(N * N) if A[i // N][i % N]]
        LB = [i // N * 100 + i % N for i in range(N * N) if B[i // N][i % N]]
        c = collections.Counter(i - j for i in LA for j in LB)
        return max(c.values() or [0])