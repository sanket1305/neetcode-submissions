class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        n = len(prices)
        cur_min = prices[0]

        for i in range(n):
            res = max(res, prices[i] - cur_min)
            cur_min = min(cur_min, prices[i])

            print(i, prices[i], cur_min, res)
        
        return res