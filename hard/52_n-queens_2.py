class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        self.n = n

        def check(x, y, queens):
            for i, j in queens:
                if j == y:
                    return False
                if x + y == i + j or x - y == i - j:
                    return False
            return True

        def find(k, queens):
            if k == 0:  
                return 1
            i = k-1
            cnt = 0
            for j in range(self.n):
                if check(i, j, queens):
                    cnt += find(k-1, queens+[(i,j)])
            return cnt

        return find(n, [])
