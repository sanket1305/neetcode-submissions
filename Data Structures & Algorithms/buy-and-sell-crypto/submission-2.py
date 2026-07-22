class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        smallest = prices[0]
        n = len(prices)

        for i in range(1, n):
            smallest = min(smallest, prices[i])
            res = max(res, prices[i] - smallest)
        
        return res