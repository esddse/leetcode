

from collections import defaultdict
from itertools import product 

class Solution:
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """

        f = defaultdict(lambda: defaultdict(list))
        for a, b, c in allowed:
            f[a][b].append(c)

        def place(bottom):
            if len(bottom) == 1:
                return True
            for next_bottom in product(*(f[a][b] for a, b in zip(bottom, bottom[1:]))):
                if place(next_bottom):
                    return True
            return False
        return place(bottom)



