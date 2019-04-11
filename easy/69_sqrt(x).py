class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        l, r = 1, x
        i = (l + r) // 2
        while i * i > x or (i+1) * (i+1) <= x:
            if i * i < x:
                l = i
            elif i * i > x:
                r = i
            i = (l + r) // 2
        return i