class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        binary = '0'+bin(N)[2:]
        last1 = None
        max_gap = 0

        for i in range(1, len(binary)):
            if binary[i] == "1":
                if last1 and i - last1 > max_gap:
                    max_gap = i - last1
                last1 = i 
        return max_gap

