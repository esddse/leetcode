import bisect
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        size = len(nums)
        l, r = 0, size-1
        if nums[r] >= nums[l]:
            idx = bisect.bisect_left(nums, target)
            if idx == size or nums[idx] != target:
                return -1 
            return idx 
        else:
            # find peak
            while l <= r:
                m = (l+r)//2
                if nums[m] > nums[m+1]:
                    peak = m
                    break
                elif nums[m] >= nums[l]:
                    l = m+1
                else:
                    r = m-1
            if target >= nums[0]:
                idx = bisect.bisect_left(nums[:peak+1], target)
            else:
                idx = bisect.bisect_left(nums[peak+1:], target) + peak + 1
            if idx == size or nums[idx] != target:
                return -1 
            return idx