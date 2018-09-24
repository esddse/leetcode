class Solution:
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        S = "122"

        last = "2"
        p = 2
        while len(S) < n:
            cnt = int(S[p])
            if last == "1":
                S += "2" * cnt
                last = "2"
            else:
                S += "1" * cnt
                last = "1"
            p += 1

        return S[:n].count("1")


