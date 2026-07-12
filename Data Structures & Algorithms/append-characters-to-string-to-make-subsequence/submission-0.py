class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        s_len, t_len = len(s), len(t)

        t_i = 0

        for i in range(s_len):
            if t_i == t_len:
                return 0

            if s[i] == t[t_i]:
                t_i += 1
        
        return t_len - t_i