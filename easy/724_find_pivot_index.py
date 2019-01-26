class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ts = sum(nums)
        ls = 0
        for i, num in enumerate(nums):
            lr = ts - ls - num
            if ls == lr:
                return i
            ls += num
        return -1