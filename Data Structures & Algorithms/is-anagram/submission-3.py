class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_map = {}
        for ch in s:
            s_map[ch] = s_map.get(ch, 0) + 1
        
        for ch in t:
            if ch not in s_map or s_map[ch] == 0:
                return False
            s_map[ch] -= 1
        
        return True