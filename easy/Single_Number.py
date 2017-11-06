class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = 0
        for num in nums:
            n ^= num
        return n
        
        
        