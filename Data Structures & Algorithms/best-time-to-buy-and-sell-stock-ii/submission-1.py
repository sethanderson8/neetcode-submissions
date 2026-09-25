class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # go reverse, two pointers, past, future
        # any time the past is lower than futuer, "sell",
        # add to max maxProfit
        # anytime the past is greater than future, future = past, past -=1
        # keep searching
        # repeat til end

        future = len(prices) - 1
        past = len(prices) - 2
        maxProf = 0

        while past >= 0:
            if prices[past] < prices[future]:
                # sell
                maxProf += (prices[future] - prices[past])
                # future is now past
            future = past
            past -= 1

        return maxProf