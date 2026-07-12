class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0

        for num in nums:
            res ^= num
        
        return res