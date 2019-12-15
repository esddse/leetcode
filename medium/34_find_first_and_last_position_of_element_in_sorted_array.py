class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
    
        if not nums:
            return [-1, -1]
        size = len(nums)
        # first
        first, last = -1, -1
        l, r = 0, size
        while l < r:
            m = (l+r)//2
            if nums[m] == target:
                if m == 0 or nums[m-1] < target:
                    first = m
                    break
                else:
                    r = m
            elif nums[m] > target:
                r = m
            else:
                l = m+1

        # last
        l, r = 0, size
        while l < r:
            m = (l+r)//2
            if nums[m] == target:
                if m == size-1 or nums[m+1] > target:
                    last = m
                    break 
                else:
                    l = m+1
            elif nums[m] > target:
                r = m 
            else:
                l = m+1
        return [first, last]