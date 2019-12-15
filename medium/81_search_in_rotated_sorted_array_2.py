class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        size = len(nums)
        # find peak
        l, r = 0, size
        while l < size and nums[l] == nums[r-1]:
            l += 1
        peak = r-1
        while l < r:
            m = (l+r)//2
            if m < size-1 and nums[m] > nums[m+1]:
                peak = m
                break
            else:
                if nums[m] >= nums[l]:
                    l = m+1
                else:
                    r = m
        # target
        transform = lambda idx: (idx+peak+1)%size 
        l, r = 0, size
        while l < r:
            m  = (l+r)//2
            tm = transform(m) 
            if nums[tm] == target:
                return True
            else:
                if target >= nums[tm]:
                    l = m+1
                else:
                    r = m
        return False



