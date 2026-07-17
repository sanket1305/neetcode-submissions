class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        first, last = 0, n-1

        while first < last:
            while first < n and not s[first].isalnum():
                first += 1
            
            while last >= 0 and not s[last].isalnum():
                last -= 1
            
            if first > last:
                return True
            
            if s[first].lower() != s[last].lower():
                return False
            
            first += 1
            last -= 1
        
        return first >= last