from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapp = defaultdict(list)
        res = []

        for s in strs:
            c = "".join(sorted([ch for ch in s]))
            mapp[c].append(s)
        
        for val in mapp.values():
            res.append(val)
        
        return res