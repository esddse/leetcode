from collections import defaultdict
class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """ 

        cnt = defaultdict(int)
        for num in nums:
            cnt[num] += 1
            if cnt[num] > 1:
                return True
        return False