class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        size = len(nums)
        nums.sort()
        s = float("inf")
        for i in range(size):
            l, r = i+1, size-1
            while l < r:
                c = nums[i]+nums[l]+nums[r]
                if abs(c-target) < abs(s-target):
                    s = c 
                if c > target:
                    r -= 1
                elif c < target:
                    l += 1
                else:
                    return s
        return s

