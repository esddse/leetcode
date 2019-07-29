class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 1:
            return 0

        size = len(prices)
        buy  = [0] * size
        sell = [0] * size

        buy[0]  = - prices[0]
        buy[1]  = - prices[1]
        sell[1] = max(0, buy[0]+prices[1])


        for i in range(2, size):
            buy[i]  = max(sell[:i-1]) - prices[i]
            sell[i] = max(buy[:i]) + prices[i]

        return max(sell)