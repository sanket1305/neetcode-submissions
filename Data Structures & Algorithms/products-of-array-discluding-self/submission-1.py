class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # left prefix product
        res = [nums[0]]
        for i in range(1, n):
            res.append(res[-1] * nums[i])
        
        right = 1
        for i in range(n-1, 0, -1):
            res[i] = res[i-1] * right
            right *= nums[i]
        
        res[0] = right

        return res