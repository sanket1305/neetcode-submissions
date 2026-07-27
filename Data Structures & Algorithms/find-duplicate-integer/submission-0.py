class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        bits = 0

        for num in nums:
            if bits & (1 << num):
                return num
            bits |= (1 << num)
        
        return bits