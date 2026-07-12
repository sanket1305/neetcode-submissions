class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        res = -1

        n = len(s)
        mapp = {}

        for i, ch in enumerate(s):
            if ch in mapp:
                res = max(res, i - mapp[ch] - 1)
            else:
                mapp[ch] = i
        
        return res