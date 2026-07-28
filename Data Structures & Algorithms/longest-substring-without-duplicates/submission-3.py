class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        charToNextIndex = {}

        for r, ch in enumerate(s):
            if ch in charToNextIndex:
                l = max(l, charToNextIndex[ch])
            res = max(res, r - l + 1)
            charToNextIndex[ch] = r + 1
        
        return res