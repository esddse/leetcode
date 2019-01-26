class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        
        s = sum(nums[:k])
        max_s = s
        for i in range(k, len(nums)):
            s += nums[i] - nums[i-k]
            max_s = max(max_s, s)
        return max_s / k