class Solution:
    def kSum(self, nums: List[int], target: int, k: int) -> List[List[int]]:
        n = len(nums)
        res = []

        # if not nums 
        if not nums:
            return res
        
        # check if avg value is out of bound
        avg_value = target//k
        if avg_value < nums[0] or avg_value > nums[-1]:
            return res
        
        if k == 2:
            return self.twoSum(nums, target)
        else:
            for i in range(n):
                if i == 0 or nums[i-1] != nums[i]:
                    for subset in self.kSum(nums[i+1:], target - nums[i], k-1):
                        res.append([nums[i]] + subset)

            return res
    
    def twoSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res = []

        # set the boundaries
        lo, hi = 0, n-1

        while lo < hi:
            curr_sum = nums[lo] + nums[hi]

            # check for duplicate as well
            if curr_sum < target or (lo > 0 and nums[lo - 1] == nums[lo]):
                lo += 1
            elif curr_sum > target or (hi < n-1 and nums[hi] == nums[hi + 1]):
                hi -= 1
            else:
                res.append([nums[lo], nums[hi]])
                lo += 1
                hi -= 1
        
        return res

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        return self.kSum(nums, target, 4)