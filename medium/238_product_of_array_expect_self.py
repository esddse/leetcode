class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        p = 1
        outputs = []
        for num in nums:
            outputs.append(p)
            p *= num

        p = 1
        for i in range(len(nums)-1, -1, -1):
            outputs[i] *= p
            p *= nums[i]

        return outputs