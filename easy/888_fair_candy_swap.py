class Solution:
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        A.sort()
        B.sort()

        sum_A = sum(A)
        sum_B = sum(B)
        
        standard = (sum_A + sum_B) / 2
        A_gap = standard - sum_A

        i, j = 0, 0
        while True:
            num_A = A[i]
            num_B = B[j]

            if num_A + A_gap == num_B:
                return [num_A, num_B]
            elif num_A + A_gap > num_B:
                j += 1
            else:
                i += 1
