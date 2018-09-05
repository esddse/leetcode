class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """

        i = 0 
        num = 0
        while i < len(bits):
            if bits[i] == 0:
                num = 1
                i += 1
            else:
                num = 2
                i += 2
        return num == 1

        