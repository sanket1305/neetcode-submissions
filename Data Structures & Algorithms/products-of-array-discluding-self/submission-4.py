class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        N = len(nums)

        res.append(1)
        for i in range(1, N):
            res.append(res[-1] * nums[i-1])
                
        R = 1
        for i in range(N-1, -1, -1):
            res[i] = res[i] * R
            R *= nums[i]
        
        return res