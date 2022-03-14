# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

DIAMETER OF BINARY TREE : LONGEST PATH BETWEEN TWO NODES, 
                          PATH SHOULD NOT BE PASS THROUGH ROOT NODE ( In counting we will deduct the count of root node )
        
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
