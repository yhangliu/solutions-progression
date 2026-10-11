# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diamater = 0

        def dfs(root):
            nonlocal diamater 
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            diamater = max(diamater, left + right)
            return max(left, right) + 1
        dfs(root)
        return diamater
        