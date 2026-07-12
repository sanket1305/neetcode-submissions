class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        nums *= 2

        c = 1
        for i in range(1, len(nums)):
            if nums[i] >= nums[i-1]:
                c += 1
            else:
                c = 1
            
            if c == n:
                return True

        return False