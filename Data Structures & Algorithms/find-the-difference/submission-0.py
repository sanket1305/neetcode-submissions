class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        c = Counter(s)

        for ch in t:
            if c[ch] == 0:
                return ch
            c[ch] -= 1
        