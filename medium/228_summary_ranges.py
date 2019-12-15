class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        ret = []
        start, prev = nums[0], nums[0]
        for curr in nums[1:]:
            if curr != prev + 1:
                if start == prev:
                    ret.append(str(start))
                else:
                    ret.append("%d->%d" % (start, prev))
                start, prev = curr, curr
            else:
                prev = curr
        if start == prev:
            ret.append(str(start))
        else:
            ret.append("%d->%d" % (start, prev))
        return ret
