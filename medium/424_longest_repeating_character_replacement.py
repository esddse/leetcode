from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = Counter()
        maxf, res = 0, 0
        for i in range(len(s)):
            counter[s[i]] += 1  
            maxf = max(maxf, counter[s[i]])
            if res - maxf < k:
                res += 1
            else:
                counter[s[i-res]] -= 1
        return res