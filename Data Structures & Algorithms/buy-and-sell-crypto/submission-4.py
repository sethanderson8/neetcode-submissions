class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Iterate over array
        # Need to keep track of lowValue and index and highValue and index, only if after index of low value

        if prices is None or len(prices) <= 1:
            return 0
        
        low = len(prices) - 1
        high = len(prices) - 1

        lowMax = low
        highMax = high
        low -= 1

        while low >= 0:
            currentDiff = prices[high] - prices[low]
            if currentDiff > (prices[highMax] - prices[lowMax]):
                lowMax = low
                highMax = high

            if prices[low] > prices[high]:
                high = low

            low -= 1

        return prices[highMax] - prices[lowMax]
            

