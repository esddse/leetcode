import math

class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        max_e = max(piles)
        min_e = math.ceil(sum(piles) / H)

        def count_h(piles, e):
            if e == 0:
                return float("inf")
            s = 0
            for pile in piles:
                s += math.ceil(pile / e)
            return s

        l, r = min_e, max_e + 1
        while l < r:
            m = int((l + r) / 2) 
            h  = count_h(piles, m)
            hm = count_h(piles, m-1)
            if h <= H:
                if hm > H:
                    return m
                else:
                    r = m
            else:
                l = m
        return m
