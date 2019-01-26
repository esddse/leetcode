class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l + r) // 2
            midnum = nums[mid]
            if midnum == target:
                return mid
            elif midnum < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1