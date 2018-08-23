class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        
        def flatten(nums):
            new_nums = []
            for row in nums:
                new_nums += row
            return new_nums

        flat = flatten(nums)

        if r * c != len(flat):
            return nums

        return [[flat[i * c + j] for j in range(c)] for i in range(r)]