class Solution:
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """

        def convert(time):
            return int(time[:2]) * 60 + int(time[3:])
        times = sorted([convert(time) for time in timePoints])
        return min([(y - x) % (24 * 60) for x, y in zip(times, times[1:]+times[:1])])
