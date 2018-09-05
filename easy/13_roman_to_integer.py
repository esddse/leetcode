class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        rom2int = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        integer = 0
        for i in range(len(s)):
            c = s[i]
            if i == len(s) - 1:
                integer += rom2int[c]
                break
            if c == "I" and (s[i+1] == "V" or s[i+1] == "X"):
                    integer -= rom2int[c]
                    continue
            if c == "X" and (s[i+1] == "L" or s[i+1] == "C"):
                    integer -= rom2int[c]
                    continue
            if c == "C" and (s[i+1] == "D" or s[i+1] == "M"):
                    integer -= rom2int[c]
                    continue
            integer += rom2int[c]
        return integer
