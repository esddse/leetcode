class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n > 0:
            while n > 1:
                n /= 3
            if n == 1:
                return True
        return False