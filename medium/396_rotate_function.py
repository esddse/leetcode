class Solution:
    def maxRotateFunction(self, A: List[int]) -> int:
        if not A:
            return 0 
        size = len(A)
        base = sum([i * a for i, a in enumerate(A)])
        sum_A = sum(A)
        max_sum = base
        for i in range(size-1, -1, -1):
            base += sum_A - size * A[i]
            max_sum = max(max_sum, base)
        return max_sum