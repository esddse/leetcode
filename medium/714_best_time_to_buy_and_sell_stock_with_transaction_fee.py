class Solution:
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        buy, sell = -float("inf"), 0
        for price in prices:
            tmp  = buy
            buy  = max(tmp, sell - price)
            sell = max(sell, tmp + price - fee)
        return sell
