class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        k = 0
        while n > k:
            k += 1
            n -= k   
        return k