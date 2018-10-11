class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def binsearch(l, r, nums, target):
            if r == l:
                if target < nums[l]:
                    return l
                else:
                    return l+1
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                return binsearch(l, mid, nums, target)
            else:
                return binsearch(mid+1, r, nums, target)

        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        return binsearch(0, len(nums), nums, target)