class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1 if x >= 0 else -1
        x, y = abs(x), 0
        while x:
            y = y * 10 + x % 10
            x //= 10
        y = y * sign
        if y > (1<<31)-1 or y < -(1<<31):
            return 0 
        return y

