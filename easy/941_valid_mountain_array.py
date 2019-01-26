class Solution:
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """

        if not A or len(A) < 3:
            return False

        for i in range(1, len(A)):
            if A[i] <= A[i-1]:
                break
        if i == 1 or (i == len(A) and A[-1] > A[-2]):
            return False
        for j in range(i, len(A)):
            if A[j] >= A[j-1]:
                return False
        return True
