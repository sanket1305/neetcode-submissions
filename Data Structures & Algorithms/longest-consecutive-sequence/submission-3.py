class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mapp = {}
        res = 0

        for num in nums:
            if not mapp.get(num, 0):
                mapp[num] = 1 + mapp.get(num - 1, 0) + mapp.get(num + 1, 0)
                mapp[num - mapp.get(num - 1, 0)] = mapp[num]
                mapp[num + mapp.get(num + 1, 0)] = mapp[num]
                res = max(res, mapp[num])

        return res