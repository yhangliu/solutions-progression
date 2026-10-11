# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:




        def dfs(root, diameter):
            if not root:
                return 0, diameter
            left, left_diam = dfs(root.left, diameter)
            right, right_diam = dfs(root.right, diameter)
            diameter = max(diameter, left_diam, right_diam, left + right)
            return max(left,right) + 1, diameter
        height, diameter = dfs(root, 0)
        return diameter

        