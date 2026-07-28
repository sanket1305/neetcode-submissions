class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for word in strs:
            res += str(len(word)) + "#" + word
        
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        N = len(s)

        i = 0
        while i < N:
            size = ""
            while s[i] != "#":
                size += s[i]
                i += 1
            i += 1
            size = int(size)

            res.append(s[i: i+size])
            i = i+size
        
        return res