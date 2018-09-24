
from collections import defaultdict
class Solution:
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        
        gap = defaultdict(int)
        for line in wall:
            dis = 0
            for brick in line[:-1]:
                dis += brick
                gap[dis] += 1
        return len(wall) - max(gap.values(), default=0)