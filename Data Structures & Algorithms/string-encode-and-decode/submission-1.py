class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s
        
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        n = len(s)

        i = 0
        while i < n:
            size = ""
            while s[i] != "#":
                size += s[i]
                i += 1
            size = int(size)
            i += 1

            res.append(s[i : i+size])
            i += size
        
        return res