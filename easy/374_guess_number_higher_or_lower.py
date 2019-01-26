# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        pick = (l + r) // 2
        res = guess(pick)
        while res:
            if res == -1:
                r = pick - 1
            else:
                l = pick + 1
            pick = (l + r) // 2
            res = guess(pick)

        return pick