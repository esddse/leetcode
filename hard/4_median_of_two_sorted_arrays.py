class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if not nums1 and not nums2:
            return None
        nums = None
        if not nums1:
            nums = nums2
        elif not nums2:
            nums = nums1
        elif nums1[0] >= nums2[-1]:
            nums = nums2 + nums1
        elif nums2[0] >= nums1[-1]:
            nums = nums1 + nums2
        # 1 array
        if nums:
            size = len(nums)
            if size % 2 == 0:
                return (nums[size//2]+nums[size//2-1]) / 2
            else:
                return nums[size//2]
        # 2 arrays
        else:
            size1, size2 = len(nums1), len(nums2)
            l1, r1, l2, r2 = 0, size1, 0, size2
            

            