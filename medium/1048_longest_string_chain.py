
from collections import defaultdict
class Solution:
    def longestStrChain(self, words: List[str]) -> int:

        size = len(words)
        d = defaultdict(list)
        for word in words:
            d[len(word)].append(word)

        def is_predecessor(a, b):
            if len(a) != len(b) - 1:
                return False
            i, j = 0, 0
            checked = False
            while i < len(a):
                if a[i] != b[j]:
                    if not checked:
                        j += 1
                        checked = True
                    else:
                        return False
                else:
                    i += 1
                    j += 1
            return True


        dp = defaultdict(int)
        for key in sorted(list(d.keys())):
            for b in d[key]:
                dp[b] = 1
                if key-1 in d:
                    for a in d[key-1]:
                        if is_predecessor(a, b):
                            dp[b] = max(dp[b], dp[a]+1)

        return max(dp.values())