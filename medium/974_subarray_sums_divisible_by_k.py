

class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        ret, s, cnt = 0, 0, [1]+[0]*K
        for a in A:
            s = (s+a)%K
            ret += cnt[s]
            cnt[s] += 1
        return ret

        