from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        size = len(s)
        cs, ct = defaultdict(int), Counter(t)
        contain_all = lambda cs, ct: all([cs[c] >= ct[c] for c in ct])
        l, r = 0, 0
        min_len, min_str = float("inf"), ""
        while l < size:
            # expand right
            while r < size and not contain_all(cs, ct):
                while r < size and s[r] not in ct:
                    r += 1
                if r < size:
                    cs[s[r]] += 1
                    r += 1
            # compress left
            while l < r and s[l] not in ct:
                l += 1
            # check length
            if contain_all(cs, ct):
                if r - l < min_len:
                    min_len = r - l 
                    min_str = s[l:r]
            # next
            if l < size:
                cs[s[l]] -= 1
                l += 1
        return min_str