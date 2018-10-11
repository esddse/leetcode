class Solution:
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        neg = False
        if num < 0:
            neg = True
            num = -num
        res = ""
        while num >= 7:
            res += str(num % 7)
            num //= 7
        res += str(num % 7)
        if neg:
            return "-" + res[::-1]
        return res[::-1]