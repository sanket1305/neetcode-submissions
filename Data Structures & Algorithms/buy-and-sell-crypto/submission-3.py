class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        lowest = prices[0]
        res = 0

        i = 1
        while i < N:
            lowest = min(lowest, prices[i])
            res = max(res, prices[i] - lowest)

            i += 1
        
        return res