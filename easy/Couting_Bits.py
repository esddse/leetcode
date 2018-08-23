class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        lst = [0]
        m = 1
        for n in range(num):
            n += 1
            if n / m == 2:
                m *= 2
            lst.append(1 + lst[n-m])
        return lst
    