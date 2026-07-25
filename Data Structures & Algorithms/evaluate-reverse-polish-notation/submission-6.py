class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token not in ["+", "-", "/", "*"]:
                stack.append(int(token))
            else:
                second, first = stack.pop(), stack.pop()
                
                res = 0
                if token == "+":
                    res = first + second
                elif token == "-":
                    res = first - second
                elif token == "*":
                    res = first * second
                else:
                    res = first / second
                
                stack.append(int(res))
                    
        return int(stack[-1])