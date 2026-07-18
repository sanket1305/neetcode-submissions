class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0

        cur_low = prices[0]

        for i in range(1, n):
            max_profit = max(max_profit, prices[i] - cur_low)
            cur_low = min(cur_low, prices[i])
        
        return max_profit