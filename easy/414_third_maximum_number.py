class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first, second, third = float("-inf"), float("-inf"), float("-inf")
        for num in nums:
            if num > first:
                third = second
                second = first
                first = num
            elif num != first and num > second:
                third = second
                second = num 
            elif num != first and num != second and num > third:
                third = num
        if third != float("-inf"):
            return third 
        return first
