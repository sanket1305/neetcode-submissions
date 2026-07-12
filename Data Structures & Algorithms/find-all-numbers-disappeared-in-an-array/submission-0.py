class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []

        nums.sort()
        i = 1

        for num in nums:
            while i < num:
                res.append(i)
                i += 1

            while i == num:
                i += 1
        
        for j in range(i, n+1):
            res.append(j)

        return res