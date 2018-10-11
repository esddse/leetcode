class Solution:
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """

        def check(p1, p2, q1, q2):
            if q1 >= p2 or p1 >= q2:
                return False
            return True
        r1x1, r1y1, r1x2, r1y2 = rec1
        r2x1, r2y1, r2x2, r2y2 = rec2
        return check(r1x1, r1x2, r2x1, r2x2) and check(r1y1, r1y2, r2y1, r2y2)