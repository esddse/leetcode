
from collections import Counter
class Solution:
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """

        counter = Counter(hand)
        for i in sorted(counter):
            if counter[i] > 0:
                for j in range(W)[::-1]:
                    counter[i + j] -= counter[i]
                    if counter[i + j] < 0:
                        return False
        return True
        
        