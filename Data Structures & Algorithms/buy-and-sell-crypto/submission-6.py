class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Iterate over array
        # Need to keep track of lowValue and index and highValue and index, only if after index of low value
        
        low = len(prices) - 1
        high = len(prices) - 1

        lowMax = low
        highMax = high

        while low >= 0:
            currentDiff = prices[high] - prices[low]
            if currentDiff > (prices[highMax] - prices[lowMax]):
                lowMax = low
                highMax = high

            if prices[low] > prices[high]:
                high = low

            low -= 1

        return prices[highMax] - prices[lowMax]
            

