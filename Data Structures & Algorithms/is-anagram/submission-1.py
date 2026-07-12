class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c = Counter(s)

        for ch in t:
            if ch not in c:
                return False
            c[ch] -= 1
            if c[ch] == 0:
                del c[ch]
        
        return False if c else True