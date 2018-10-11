class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """

        while num > 1:
            num /= 4
        if num == 1:
            return True
        return False