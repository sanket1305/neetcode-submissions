class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        N = len(s)
        res = 0

        charSet = set(s)

        # for each char, find max window
        for ch in charSet:
            # count maintains the count for only curr char
            count = l = 0

            for r in range(N):
                if s[r] == ch:
                    count += 1
                
                # while we do not meet req, move left pointer
                while (r - l + 1) - count > k:
                    if s[l] == ch:
                        count -= 1
                    l += 1
                
                # update res
                res = max(res, r - l + 1)
        
        return res