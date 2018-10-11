class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        i, j = 0, len(nums)
        while i < j:
            if nums[i] == val:
                while i < j and (j == len(nums) or nums[j] == val):
                    j -= 1
                if i == j:
                    break
                nums[i], nums[j] = nums[j], nums[i]
            i += 1
        return i