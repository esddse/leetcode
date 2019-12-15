from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        size = len(s)
        
        i, j, max_l, cnter = 0, 0, 0, defaultdict(int)
        while j < size:
            if i < j:
                cnter[s[i]] -= 1
                i += 1
            while j < size and cnter[s[j]] == 0:
                cnter[s[j]] += 1
                j += 1
            print(i, j)
            max_l = max(max_l, j-i)

        return max_l


