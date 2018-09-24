class Solution:
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs = sorted(pairs, key=lambda pair: pair[1])
        cur, res = -float("inf"), 0
        for start, end in pairs:
            if start > cur:
                cur = end
                res += 1
        return res
        