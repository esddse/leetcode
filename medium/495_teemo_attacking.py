class Solution:
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        
        total, last = 0, 0

        for time in timeSeries:
            if time >= last:
                last = time + duration
                total += duration
            else:
                total += time + duration - last
                last = time + duration
        return total