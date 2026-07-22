class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # if t is empty return ""
        if t == "":
            return t
        
        # counters for t and window
        countT, window = {}, {}

        # count chars in t
        for ch in t:
            countT[ch] = 1 + countT.get(ch, 0)
        
        # setup count for have and need
        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("inf")

        # sliding window
        l = 0
        for r in range(len(s)):
            # update the count for window
            ch = s[r]
            window[ch] = 1 + window.get(ch, 0)

            # update have count
            if ch in countT and countT[ch] == window[ch]:
                have += 1

            # while have == need reduce window from left side
            while have == need:
                # if cur window is smallest, update res
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                # reduce window from left side
                window[s[l]] -= 1

                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                
                l += 1
        
        l, r = res
        return s[l: r + 1] if resLen != float("inf") else ""