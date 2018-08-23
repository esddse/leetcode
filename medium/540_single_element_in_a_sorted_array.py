class Solution:
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter

        counter = Counter(nums)
    
        for num, cnt in counter.items():
            if cnt == 1:
                return num