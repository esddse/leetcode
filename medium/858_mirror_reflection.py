import math

class Solution:
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        
        g = math.gcd(p, q)
        p /= g
        q /= g 

        if p % 2 == 0:
            bottom = '*'
        else:
            bottom = 0

        if bottom == '*':
            return 2
        else:
            if q % 2 == 0:
                return 0
            else:
                return 1

