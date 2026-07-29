class Solution:
    def isValid(self, s: str) -> bool:
        mapp = {
            '}': '{',
            ']': '[',
            ')': "("
        }

        stack = []
        for ch in s:
            if ch not in mapp:
                stack.append(ch)
            else:
                if not stack or mapp[ch] != stack[-1]:
                    return False
                stack.pop()
        
        return True if not stack else False