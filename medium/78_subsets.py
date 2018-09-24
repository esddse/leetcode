
import copy
class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        def addone(sets, num):
            origin = copy.deepcopy(sets)
            for lst in sets:
                lst.append(num)
            return origin + sets
        sets = [[]]
        for num in nums:
            sets = addone(sets, num)
        return sets