class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        
        self.combs = []
        def find(k, m, n, path):
            if k == 1:
                if n >= m and n <= 9:
                    path.append(n)
                    self.combs.append(path)
                return
            for num in range(m, n-m):
                find(k-1, num+1, n-num, path+[num])
        find(k, 1, n, [])
        return self.combs