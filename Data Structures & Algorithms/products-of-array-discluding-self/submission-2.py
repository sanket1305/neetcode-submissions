class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        res = [nums[0]]
        for i in range(1, n):
            res.append(res[-1] * nums[i])
        
        R = 1
        for i in range(n-1, 0, -1):
            res[i] = res[i-1] * R
            R *= nums[i]
        
        res[0] = R
        return res