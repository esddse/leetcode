class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        s = 0
        m = 5
        while m <= n:
            s += n // m
            m *= 5
        return s