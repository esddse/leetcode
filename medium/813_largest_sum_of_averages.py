class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:

        mem = {}
        def search(n, k):
            if (n, k) in mem:
                return mem[n, k]
            if k > n:
                return 0
            if k == 1:
                mem[n, k] = sum(A[:n]) / n
                return mem[n, k]
            s, mem[n, k] = 0, 0
            for i in range(n-1, 0, -1):
                s += A[i]
                mem[n, k] = max(mem[n, k], search(i, k-1) + s / (n-i))

            return mem[n, k]

        return search(len(A), K)