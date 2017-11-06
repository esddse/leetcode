class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_num = min(nums)
        cnt = 0
        for num in nums:
            cnt += num-min_num
        return cnt