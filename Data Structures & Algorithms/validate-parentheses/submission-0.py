class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        mapp = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        stack = []
        for i, ch in enumerate(s):
            if ch in mapp:
                if stack and stack[-1] == mapp[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        
        return False if stack else True