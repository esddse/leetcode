class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        N = len(prices)
        min_buy = prices[0]
        max_profit = 0
        for p in prices:
            min_buy = min(min_buy, p)
            max_profit = max(p - min_buy, max_profit)
        return max_profit
