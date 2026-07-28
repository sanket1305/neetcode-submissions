class Solution:
    def isPalindrome(self, s: str) -> bool:
        N = len(s)

        lo, hi = 0, N-1
        while(lo < hi):
            while lo < N and not s[lo].isalnum():
                lo += 1
            
            while hi >= 0 and not s[hi].isalnum():
                hi -= 1
            
            if lo < hi and s[lo].lower() != s[hi].lower():
                return False
            lo += 1
            hi -= 1
        
        return True