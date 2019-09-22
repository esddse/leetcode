
import bisect
class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:

        Ap = [0] * len(A)
        As, Bs = sorted(A), sorted(enumerate(B), key=lambda item: item[1])
        for i, b in Bs:
            idx = bisect.bisect_right(As, b)
            if idx == len(As):
                Ap[i] = As[0]
                As.pop(0)
            else:
                Ap[i] = As[idx]
                As.pop(idx)
        return Ap