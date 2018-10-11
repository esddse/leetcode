class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        s = set()
        while True:
            n = sum([int(i) ** 2 for i in str(n)])
            if n == 1:
                return True
            else:
                if n in s:
                    return False
                s.add(n)