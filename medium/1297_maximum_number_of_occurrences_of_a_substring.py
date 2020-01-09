from collections import Counter
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        size = len(s)
        substr_counter = Counter()
        cha_counter = Counter()
        charnum = 0
        max_occur = 0
        for i in range(size-minSize+1):
            substr = s[i:i+minSize]
            if i == 0:
                cha_counter.update(substr)
                charnum = len(cha_counter)
            else:
                deletec, addc = s[i-1], substr[-1]
                cha_counter[deletec] -= 1
                if cha_counter[deletec] == 0:
                    charnum -= 1
                cha_counter[addc] += 1
                if cha_counter[addc] == 1:
                    charnum += 1
            if charnum > maxLetters:
                continue 
            substr_counter[substr] += 1
            max_occur = max(max_occur, substr_counter[substr])
        return max_occur