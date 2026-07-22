class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # counters for t and window
        countT, window = {}, {}

        for ch in t:
            countT[ch] = 1 + countT.get(ch, 0)
        
        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("inf")

        l = 0
        for r in range(len(s)):
            ch = s[r]
            window[ch] = 1 + window.get(ch, 0)

            if ch in countT and countT[ch] == window[ch]:
                have += 1
            
            while have == need:
                # update res
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        
        l, r = res
        return s[l: r+1] if resLen != float("inf") else ""