
from collections import Counter
class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        b_counter = Counter()
        for b in B:
            for letter, cnt in Counter(b).items():
                if letter in b_counter:
                    b_counter[letter] = max(b_counter[letter], cnt)
                else:
                    b_counter[letter] = cnt
        res = []
        for a in A:
            a_counter = Counter(a)
            flag = True
            for letter, cnt in b_counter.items():
                if a_counter[letter] < cnt:
                    flag = False
                    break
            if flag:
                res.append(a)
        return res
