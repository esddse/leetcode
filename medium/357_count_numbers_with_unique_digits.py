class Solution:
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        if n > 10:
            n = 10
        base = [9, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        ans, num = 1, 1
        for i in range(n):
            num *= base[i]
            ans += num
        return ans
        
