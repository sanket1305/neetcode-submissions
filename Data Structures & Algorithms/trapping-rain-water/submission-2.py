class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        n = len(height)

        leftmax = rightmax = 0
        left, right = 0, n - 1

        while left < right:
            if height[left] < height[right]:
                leftmax = max(leftmax, height[left])
                res += leftmax - height[left]
                left += 1
            else:
                rightmax = max(rightmax, height[right])
                res += rightmax - height[right]
                right -= 1
        
        return res