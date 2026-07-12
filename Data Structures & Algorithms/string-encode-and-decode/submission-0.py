class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []

        for s in strs:
            res.append(str(len(s)) + "#" + s)
        
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []

        n = len(s)
        i = 0

        while i < n:
            size = ""

            while s[i] != "#":
                size += s[i]
                i += 1
            
            i += 1
            res.append(s[i:i+int(size)])

            i += int(size)
        
        return res