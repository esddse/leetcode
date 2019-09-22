import bisect
from collections import defaultdict
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return None
        size = len(nums)
        
        subseqs = defaultdict(set)
        subseqs[nums[0]].add((nums[0],))

        lasts = [nums[0]]
        for num in nums[1:]:
            idx = bisect.bisect_right(lasts, num)
            new_seqs = set()
            for last in lasts[:idx]:
                for seq in subseqs[last]:
                    new_seqs.add(seq+(num,))
            subseqs[num].update(new_seqs)
            subseqs[num].add((num,))
            lasts.insert(idx, num)


        res = set()
        for k, v in subseqs.items():
            res.update(v)
        return map(list, [item for item in res if len(item) >= 2])

