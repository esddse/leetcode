
from collections import defaultdict
class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        d = defaultdict(list)
        for word in words:
            word = iter(word)
            d[next(word)].append(word)

        for s in S:
            ds = []
            for word in d[s]:
                c = next(word, "")
                if c == s:
                    ds.append(word)
                else:
                    d[c].append(word)
            d[s] = ds

        return len(d[""])      
