class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for word in strs:
            freq = [0] * 26
            for ch in word:
                freq[ord(ch) - ord('a')] += 1
            
            if tuple(freq) not in res:
                res[tuple(freq)] = [word]
            else:
                res[tuple(freq)].append(word)
        
        return [list(x) for x in res.values()]