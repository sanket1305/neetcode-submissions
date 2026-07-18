class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mapp = defaultdict(int)
        res = 0

        for num in nums:
            if not mapp[num]:
                mapp[num] = 1 + mapp[num - 1] + mapp[num + 1]
                mapp[num - mapp[num - 1]] = mapp[num]
                mapp[num + mapp[num + 1]] = mapp[num]
                res = max(res, mapp[num])

        return res