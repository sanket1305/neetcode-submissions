class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        c = Counter(text)

        res = float("inf")

        for ch in ['b', 'a', 'n']:
            res = min(res, c[ch])
        
        for ch in ['l', 'o']:
            res = min(res, c[ch]//2)
        
        return res