class StockSpanner:

    def __init__(self):
        self.prices = []
        

    def next(self, price: int) -> int:
        self.prices.append(price)
        i = len(self.prices) - 2
        while i >= 0 and self.prices[i] <= price:
            i -= 1
        return len(self.prices) - i - 1


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)