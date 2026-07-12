class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        N = len(heights)
        
        first, last = 0, N-1
        while first < last:
            res = max(res, min(heights[first], heights[last]) * (last - first))

            if heights[first] > heights[last]:
                last -= 1
            else:
                first += 1

        return res