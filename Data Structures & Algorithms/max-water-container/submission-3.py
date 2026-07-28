class Solution:
    def maxArea(self, heights: List[int]) -> int:
        N = len(heights)
        lo, hi = 0, N-1

        res = 0
        while lo < hi:
            res = max(res, (hi - lo) * min(heights[lo], heights[hi]))
            
            if heights[lo] < heights[hi]:
                lo += 1
            else:
                hi -= 1
        
        return res