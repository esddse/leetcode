class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
    
        for p in [2, 3, 5]:
            while num > 1 and num % p == 0:
                num //= p
        return num == 1