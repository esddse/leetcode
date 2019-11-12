from collections import Counter
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        max_len = 0
        for cnum in range(1, 27):
            i, j = 0, 0
            ccnt = 0
            counter = Counter()
            while j < len(s):
                if ccnt <= cnum:
                    if not counter[s[j]]:
                        ccnt += 1
                    counter[s[j]] += 1
                    j += 1
                else:
                    counter[s[i]] -= 1
                    if not counter[s[i]]:
                        ccnt -= 1
                    i += 1
                if ccnt == cnum:
                    valid = True
                    for c, cnt in counter.items():
                        if 0 < cnt < k:
                            valid = False 
                            break
                    if valid:
                        max_len = max(max_len, j-i)
        return max_len
