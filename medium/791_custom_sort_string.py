class Solution:
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        val = {}
        for c in alphabet:
            val[c] = -1
        for i, c in enumerate(S):
            val[c] = i
        T = sorted(T, key=lambda c: val[c])
        return "".join(T)