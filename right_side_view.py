# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightView(self, node, level, ls):
        if node is None:
            return 
        if len(ls) == level:
            ls.append(node.val)
        self.rightView(node.right, level+1, ls)
        self.rightView(node.left, level+1, ls)
    
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        level = 0
        ls = []
        self.rightView(root, level, ls)
        return ls
