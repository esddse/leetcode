
from collections import Counter
class Solution:
    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """

        counter_n  = Counter(str(N))
        counter_2s = [Counter(str(1 << i)) for i in range(32)]
        return counter_n in counter_2s 
