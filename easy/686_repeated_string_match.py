
import math
class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        lower_bound = int(math.ceil(len(B) / len(A)))
        if B in A * lower_bound:
            return lower_bound
        if B in A * (lower_bound + 1):
            return lower_bound + 1
        return -1
