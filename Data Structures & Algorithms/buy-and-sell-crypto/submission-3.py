class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1: return 0

        i, j = 0, 1
        max_profit = 0
        while i < len(prices) and j < len(prices):
            while i < len(prices) and prices[j] < prices[i]: 
                i += 1
            
            j = i+1
            while j < len(prices) and prices[j] > prices[i]:
                max_profit = max(max_profit, prices[j] - prices[i])
                j += 1

            i += 1
            if i == len(prices): break

        return max_profit

