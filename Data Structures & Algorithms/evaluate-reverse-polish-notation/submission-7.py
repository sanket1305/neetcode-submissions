class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t not in ["+", "-", "/", "*"]:
                stack.append(int(t))
            else:
                second, first = stack.pop(), stack.pop()

                if t == "+":
                    stack.append(first + second)
                elif t == "-":
                    stack.append(first - second)
                elif t == "*":
                    stack.append(first * second)
                elif t == "/":
                    stack.append(int(first / second))
        
        return stack[0]