class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1 = set(nums1)
        nums2 = set(nums2)

        output = set([])
        for num in nums1:
            if num in nums2:
                output.add(num)
        return list(output)