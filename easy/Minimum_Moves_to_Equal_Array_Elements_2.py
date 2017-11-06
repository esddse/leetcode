class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        i = 0
        j = len(nums) - 1
        cnt = 0
        while i < j:
            cnt += nums[j] - nums[i]
            i += 1
            j -= 1
        return cnt