class Solution:
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        s = 0
        for i in range(32):
            zero_ones = [num >> i & 1 for num in nums]
            cnt0 = zero_ones.count(0)
            cnt1 = len(zero_ones) - cnt0
            s += cnt0 * cnt1
        return s