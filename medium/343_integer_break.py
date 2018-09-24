class Solution:
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n == 2:
            return 1
        if n == 3:
            return 2
        if n == 4:
            return 4
        if n == 5:
            return 6
        re = n % 3
        if re == 0:
            return 3 ** (n // 3)
        if re == 1:
            return 3 ** (n // 3 - 1) * 4
        if re == 2:
            return 3 ** (n // 3) * 2 