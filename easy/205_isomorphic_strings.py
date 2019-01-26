class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        s2t, t2s = {}, {}
        for i in range(len(s)):
            si, ti = s[i], t[i]
            if si in s2t:
                if ti != s2t[si]:
                    return False
            elif ti in t2s:
                return False
            else:
                s2t[si], t2s[ti] = ti, si
        return True
