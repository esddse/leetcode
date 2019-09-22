from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cummu_cnt = defaultdict(int)
        cummu_cnt[0] = 1
        cummu = 0
        res = 0
        for num in nums:
            cummu += num
            if cummu - k in cummu_cnt:
                res += cummu_cnt[cummu-k]
            cummu_cnt[cummu] += 1
        return res