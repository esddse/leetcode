class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        max_num = float("-inf")
        sec_num = float("-inf")
        max_idx = -1

        for i, num in enumerate(nums):
            if num > max_num:
                sec_num = max_num
                max_num = num
                max_idx = i
            elif num > sec_num:
                sec_num = num

        if max_num >= 2 * sec_num:
            return max_idx
        return -1 