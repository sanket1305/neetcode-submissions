class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []

        res = [0]*len(temperatures)

        for idx, tmp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < tmp:
                res[stack[-1]] = idx - stack[-1]
                stack.pop()
            stack.append(idx)
        
        return res