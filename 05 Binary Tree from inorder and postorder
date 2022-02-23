# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def build(self, postorder, d, beg, end):
        if beg > end: 
            return None
        root = TreeNode(postorder.pop())
        index = d[root.val]
        root.right = self.build(postorder, d, index+1, end)
        root.left = self.build(postorder, d, beg, index-1)
        
        return root
        
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        d = {v:i for i,v in enumerate(inorder)}
        return self.build(postorder, d, 0, len(inorder)-1)
    
