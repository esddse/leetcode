class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """

        check = [False] * n
        cnt = 0
        for i in range(2, n):
            if not check[i]:
                cnt += 1
                for j in range(i, n, i):
                    check[j] = True
            else:
                continue
        return cnt