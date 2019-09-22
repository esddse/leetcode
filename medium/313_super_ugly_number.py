import heapq
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ugly_nums = [1]
        candidates = []
        while len(ugly_nums) < n:
            last_num = ugly_nums[-1]
            for prime in primes:
                heapq.heappush(candidates, prime*last_num)
            while candidates[0] == ugly_nums[-1]:
                heapq.heappop(candidates)
            ugly_nums.append(heapq.heappop(candidates))
        return ugly_nums[-1]