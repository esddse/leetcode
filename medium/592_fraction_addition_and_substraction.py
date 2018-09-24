
import math
import re
class Solution:
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        
        nums = list(map(int, re.findall('[+-]?\d+', expression)))

        A, B = 0, 1
        for a, b in zip(nums[::2], nums[1::2]):
            A = A * b + a * B
            B = B * b
            g = math.gcd(A, B)
            A //= g
            B //= g 
        return "%d/%d" % (A, B)