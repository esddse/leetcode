from collections import Counter
class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """

        len_s, len_p = len(s), len(p)
        counter_p = Counter(p)
        counter_s = Counter(s[:len_p])
        if counter_p == counter_s:
            res = [0]
        else:
            res = []
        for i in range(len_p, len_s):
            counter_s[s[i]] += 1
            counter_s[s[i-len_p]] -= 1
            if counter_s[s[i-len_p]] == 0:
                del counter_s[s[i-len_p]]
            if counter_s == counter_p:
                res.append(i-len_p+1)
        return res
        