class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        ds = {}
        dt = {}
        for c in s:
            if c in ds:
                ds[c] += 1
            else:
                ds[c] = 1
        ds = sorted(ds.items(), key = lambda item: item[0])
        
        for c in t:
            if c in dt:
                dt[c] += 1
            else:
                dt[c] = 1
        dt = sorted(dt.items(), key = lambda item: item[0])
        
        
        for i in range(len(ds)):
            if ds[i][0] != dt[i][0] or ds[i][1] != dt[i][1]:
                return dt[i][0]
        return dt[-1][0]
        