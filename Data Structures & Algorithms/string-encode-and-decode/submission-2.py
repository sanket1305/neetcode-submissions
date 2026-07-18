class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for word in strs:
            res += str(len(word)) + "#" + word

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
            i += 1

            res.append(s[i: i + int(size)])
            i = i + int(size)
        
        return res