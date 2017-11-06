class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        d = {}
        for c in s:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
        d = sorted(d.items(), key = lambda item : item[1], reverse = True)
        s = ''
        for item in d:
            s += item[0]*item[1]
        return s
            
        