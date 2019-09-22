class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums = [-float("inf")] + nums + [-float("inf")]

        def check(i):
            if nums[i-1] < nums[i] and nums[i] > nums[i+1]:
                return True 
            return False

        l, r = 0, len(nums)-1
        while l <= r:
            m = (l+r) // 2
            if check(m):
                return m-1
            else:
                if nums[m-1] < nums[m+1]:
                    l = m+1
                else:
                    r = m-1


