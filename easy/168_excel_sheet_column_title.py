class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """

        ret = ""
        while n:
            ret = chr((n-1)%26+65) + ret 
            n = (n-1) // 26
        return ret