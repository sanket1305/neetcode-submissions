class Solution:
    def search(self, nums: List[int], target: int) -> int:
        N = len(nums)
        l, r = 0, N-1

        while l < r:
            mid = (l + r)//2

            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
            
            print(l, r)
        
        return l if nums[l] == target else -1