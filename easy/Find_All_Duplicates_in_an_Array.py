class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d = {}
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        l = []

        for key, value in d.items():
            if value == 2:
                l.append(key)
                
        return l
    
        
        