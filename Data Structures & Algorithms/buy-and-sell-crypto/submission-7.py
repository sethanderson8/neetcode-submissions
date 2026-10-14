class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = right = len(prices) - 1
        max_profit = 0

        while left >= 0:
            if prices[left] >= prices[right]:
                right = left
            else:
                max_profit = max(max_profit, prices[right] - prices[left])

            left -= 1

        return max_profit

        # [10,1,5,6,7,1]
        #   l    
        #   r            
        # max_profit = 6
        