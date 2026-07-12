# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = 0
    
    def dfs(self, curr: int, node: Optional[TreeNode]):
        if node:
            if not node.left and not node.right:
                self.res += (10 * curr + node.val)
            else:
                self.dfs(10 * curr + node.val, node.left)
                self.dfs(10 * curr + node.val, node.right)

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.dfs(0, root)

        return self.res