class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []

        prod = 1
        for num in nums:
            prod *= num
            res.append(prod)
        
        R = 1
        for i in range(n-1, 0, -1):
            res[i] = res[i-1] * R
            R *= nums[i]
        
        res[0] = R
        return res