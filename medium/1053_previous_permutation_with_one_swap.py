class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        
        size = len(A)
        if size < 2:
            return A

        min_num = float("inf")
        min_after = {}
        for i in range(size-1, -1, -1):
            min_after[i] = min_num
            min_num = min(min_num, A[i])

        for i in range(size-2, -1, -1):
            if min_after[i] >= A[i]:
                continue
            else:
                max_num = float("-inf")
                max_j = 0
                for j in range(i+1, size):
                    if A[j] >= A[i]:
                        continue
                    if A[j] > max_num:
                        max_j = j
                        max_num = A[j]
                A[i], A[max_j] = A[max_j], A[i]
                return A

        return A