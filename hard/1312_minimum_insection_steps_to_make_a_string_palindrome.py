class Solution:
    def minInsertions(self, s: str) -> int:
        d = {}
        def find(s, d):
            if not s or len(s) == 1:
                return 0
            if s in d:
                return d[s] 
            size = len(s)
            i, j = 0, size-1
            while i <= j and s[i] == s[j]:
                i += 1
                j -= 1
            if i >= j:
                return 0
            ds = 1 + min(find(s[i: j], d), find(s[i+1: j+1], d))
            d[s] = ds
            return ds  
        return find(s, d)