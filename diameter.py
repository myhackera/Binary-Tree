# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def heightOfTree(node):
            nonlocal diameter
            if(not node):
                return 0
            lh = heightOfTree(node.left)
            rh = heightOfTree(node.right)
            diameter = max(diameter, lh+rh)
            return 1 + max(lh,rh)
        
        diameter = 0
        heightOfTree(root)
        return diameter