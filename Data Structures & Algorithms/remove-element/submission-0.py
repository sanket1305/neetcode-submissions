class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)

        j = 0
        while j < n and nums[j] != val:
            j += 1
        
        i = j
        while j < n:
            while j < n and nums[j] == val:
                j += 1
            
            if j == n:
                break
            
            nums[i] = nums[j]
            i += 1
            j += 1
        
        return i
            