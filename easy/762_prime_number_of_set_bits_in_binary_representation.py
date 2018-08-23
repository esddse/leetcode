
class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """

        Cnt = 0
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        for num in range(L, R+1):
            cnt = 0
            for i in bin(num):
                if i == "1":
                    cnt += 1
            if cnt in primes:
                Cnt += 1
        return Cnt