class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        def rec(i, curr):
            if i == n:
                res.append(curr)
            else:
                rec(i + 1, curr.copy())
                curr.append(nums[i])
                rec(i + 1, curr.copy())

        rec(0, [])
        return res