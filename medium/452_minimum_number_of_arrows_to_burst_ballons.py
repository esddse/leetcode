class Solution:
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        N = len(points)
        points = sorted(points, key=lambda p: p[1])
        cnt, end = 0, float("-inf")
        for p in points:
            if p[0] > end:
                cnt += 1
                end = p[1]
        return cnt