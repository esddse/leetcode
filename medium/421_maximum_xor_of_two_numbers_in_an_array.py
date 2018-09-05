class Solution:
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        def exist(prefixes, accu):
            for prefix in prefixes:
                if accu ^ 1 ^ prefix in prefixes:
                    return True
            return False 


        accu = 0
        for i in reversed(range(32)):
            accu <<= 1
            prefixes = {num >> i for num in nums}
            if exist(prefixes, accu):
                accu += 1
        return accu