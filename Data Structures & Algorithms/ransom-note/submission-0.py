class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mapp = Counter(magazine)

        for ch in ransomNote:
            if ch in mapp and mapp[ch] > 0:
                mapp[ch] -= 1
            else:
                return False
        
        return True