class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        y = 0
        while x:
            y = y * 10 + x % 10
            x //= 10
        return y

