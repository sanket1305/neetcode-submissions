class Solution:
    def findLucky(self, arr: List[int]) -> int:
        c = Counter(arr)
        res = -1

        for key, val in c.items():
            if key == val:
                res = max(res, key)
        
        return res