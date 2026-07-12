class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []

        pt = 0
        while pt < n and nums[pt] < 0:
            pt += 1
        
        lo, hi = pt-1, pt
        while lo >= 0 and hi < n:
            if nums[lo]**2 > nums[hi]**2:
                res.append(nums[hi]**2)
                hi += 1
            else:
                res.append(nums[lo]**2)
                lo -= 1
        
        while lo >= 0:
            res.append(nums[lo]**2)
            lo -= 1
        
        while hi < n:
            res.append(nums[hi]**2)
            hi += 1
        
        return res