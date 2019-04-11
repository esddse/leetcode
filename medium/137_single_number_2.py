class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a, b = 0, 0
        for num in nums:
            b = b ^ num & ~a
            a = a ^ num & ~b
        return a | b