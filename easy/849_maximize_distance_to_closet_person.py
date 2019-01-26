class Solution:
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        
        last1 = -1
        max_dist = 0
        for i, seat in enumerate(seats):
            if seat == 1:
                if last1 == -1:
                    max_dist = max(max_dist, i)
                else:
                    zero_num = i - last1 - 1
                    max_dist = max(max_dist, (zero_num + 1) // 2)
                last1 = i 
        max_dist = max(max_dist, len(seats) - last1 - 1)
        return max_dist
