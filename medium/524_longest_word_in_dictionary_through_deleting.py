from functools import cmp_to_key
class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        
        def cmp_func(x, y):
            lx, ly = len(x), len(y)
            if lx < ly:
                return 1 
            elif lx == ly:
                if x > y:
                    return 1
            return -1   
        d = sorted(d, key=cmp_to_key(cmp_func))
        
        def check_subseq(a, b):
            i, j = 0, 0
            lena, lenb = len(a), len(b)
            while i < lena and j < lenb:
                if a[i] == b[j]:
                    i += 1
                    j += 1
                else:
                    i += 1
            if j == lenb:
                return True 
            return False

        for c in d:
            if check_subseq(s, c):
                return c 
        return ""