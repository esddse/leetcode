from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = len(s1)
        c1 = Counter(s1)
        c2 = Counter(s2[:l])
        if c1 == c2:
            return True
        s, e = 0, l
        while e < len(s2):
            c2[s2[s]] -= 1
            if not c2[s2[s]]:
                del c2[s2[s]]
            c2[s2[e]] += 1
            if c1 == c2:
                return True 
            s += 1
            e += 1
        return False

