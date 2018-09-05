class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        
        if not A and not B:
            return True

        for i in range(len(A)):
            string = A[i:] + A[:i]
            if string == B:
                return True
        return False