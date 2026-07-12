class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1, n2 = len(word1), len(word2)
        i = 0
        res = []

        while i < n1 and i < n2:
            res.append(word1[i])
            res.append(word2[i])

            i += 1
        
        while i < n1:
            res.append(word1[i])
            i += 1
        
        while i < n2:
            res.append(word2[i])
            i += 1

        return "".join(res)