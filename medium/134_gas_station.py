class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if not gas or not cost:
            return -1
        size = len(gas)
        diff = [gas[i] - cost[i] for i in range(size)]
        if sum(diff) < 0:
            return -1
        
        step, p, oil = 0, 0, 0
        while step < size:
            step, oil = 0, 0
            # find start：
            while diff[p] < 0:
                p = (p+1)%size
            # travel 
            while step < size and oil >= 0:
                oil += diff[p]
                p = (p+1)%size
                step += 1
        return p
            