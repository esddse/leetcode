import math
class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """

        even = True
        new_s = ""
        n = math.ceil(len(s)/k) 
        for i in range(n):
            substr = s[i*k:i*k+k]
            if even:
                substr = substr[::-1]
            new_s += substr
            even = not even
        return new_s