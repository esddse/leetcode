
from collections import Counter
class Solution:

    

    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        def gcd(a, b):
            while b > 0:
                a, b = b, a % b
            return a
        
        counter = Counter(deck)
        k = None
        for num, cnt in counter.items():
            if cnt < 2:
                return False
            if not k:
                k = cnt
            else:
                k = gcd(k, cnt)
                if k < 2:
                    return False
        return True