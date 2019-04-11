# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        l, r = 1, n
        while True:
            m = (l + r) // 2
            check_m = isBadVersion(m)
            if check_m:
                if not isBadVersion(m-1):
                    return m
                r = m - 1
            else:
                if isBadVersion(m+1):
                    return m+1
                l = m + 1
