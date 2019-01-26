class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        
        squared_set = set()
        i = 0
        while i * i <= c:
            squared_set.add(i*i)
            i += 1
        for i in squared_set:
            if c - i in squared_set:
                return True
        return False