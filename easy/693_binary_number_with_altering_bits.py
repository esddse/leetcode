class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """

        binary = bin(n)[2:]
        last = binary[0]
        for i in range(1, len(binary)):
            if binary[i] == last:
                return False
            last = binary[i]
        return True

        