class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        num2pos = {}
        for i, num in enumerate(nums2):
            num2pos[num] = i

        outputs = []
        for num in nums1:
            pos = num2pos[num]
            found = False
            for i in range(pos+1, len(nums2)):
                if nums2[i] > num:
                    outputs.append(nums2[i])
                    found = True
                    break
            if not found:
                outputs.append(-1)

        return outputs

        