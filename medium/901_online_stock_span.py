class StockSpanner:

    def __init__(self):
        self.prices = []
        self.days = []

    def next(self, price: int) -> int:
        
        if not self.prices:
            self.prices.append(price)
            self.days.append(1)
            return 1

        day = 1
        idx = len(self.prices)-1
        while idx >= 0 and price >= self.prices[idx]:
            day += self.days[idx]
            idx -= self.days[idx]
        self.prices.append(price)
        self.days.append(day) 
        return day


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)