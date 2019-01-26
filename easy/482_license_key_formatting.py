class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        
        S = "".join(S.split("-")).upper()
        lst = reversed([S[max(i-K, 0):i] for i in range(len(S), 0, -K)])
        return "-".join(lst)
