class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0 
        leftMax = rightMax = 0

        left, right = 0, len(height) - 1

        while left < right:
            if height[left] < height[right]:
                leftMax = max(height[left], leftMax)
                res += leftMax - height[left]
                left += 1
            else:
                rightMax = max(height[right], rightMax)
                res += rightMax - height[right]
                right -= 1
        
        return res