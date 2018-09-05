
import math
from collections import Counter

class Solution:
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        
        counter = Counter([answer+1 for answer in answers])
        s = 0
        for num, cnt in counter.items():
            s += num * math.ceil(cnt/num)
        return s