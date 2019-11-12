class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        time_dist = [((target-p)/s, (target-p)) for p, s in zip(position, speed)]
        time_dist = sorted(time_dist, key=lambda item: item[1])

        fleet_cnt  = 0
        fleet_time = 0
        for t, d in time_dist:
            if t > fleet_time:
                fleet_cnt += 1
                fleet_time = t 
        return fleet_cnt
