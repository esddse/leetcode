class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        s = 0
        pre = prices[0]
        for cur in prices[1:]:
            if cur > pre:
                s += cur - pre
            pre = cur
        return s