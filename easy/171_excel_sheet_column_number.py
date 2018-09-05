class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        base = 1
        col = 0
        for c in s[-1::-1]:
            c = ord(c) - 64
            col += c * base
            base *= 26
        return col