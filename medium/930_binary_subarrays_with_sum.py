from collections import Counter

class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        sum_cnt = Counter()
        sum_cnt[0] = 1
        s = 0
        cnt = 0
        for a in A:
            s += a
            cnt += sum_cnt[s-S]
            sum_cnt[s] += 1
        return cnt