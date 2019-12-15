
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        if size < 3:
            return []
        nums = sorted(nums)
        ret = []
        for i in range(size-2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, size-1
            while l < r:
                sum2 = nums[l] + nums[r]
                if sum2 == -nums[i]:
                    ret.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1 
                elif sum2 > -nums[i]:
                    r -= 1
                else:
                    l += 1
        return ret

                
