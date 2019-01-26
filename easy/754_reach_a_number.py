class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        target = abs(target)
        s, i = 0, 0
        while s < target or (s > target and (s-target) % 2 == 1):
            i += 1
            s += i 
        return i