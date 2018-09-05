class Solution:
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        
        res = 0
        for p in points:
            len_cnt = {}
            for q in points:
                length = (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2
                len_cnt[length] = len_cnt.get(length, 0) + 1
            for lengh, cnt in len_cnt.items():
                res += cnt * (cnt-1)
        return res