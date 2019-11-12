class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        N = len(A)
        if N <= 2:
            return True 
        max_num = 0
        for i in range(2, N): 
            max_num = max(max_num, A[i-2])
            if max_num > A[i]:
                return False 
        return True
