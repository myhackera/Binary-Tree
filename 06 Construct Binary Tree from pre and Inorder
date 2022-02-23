# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# USING DICTIONARY ( FAST )
class Solution:
    def build(self, preorder, d, beg, end):
        if beg > end:
            return None
        root = TreeNode(preorder.pop())
        index = d[root.val]
        root.left = self.build(preorder, d, beg, index-1)
        root.right = self.build(preorder, d, index+1, end)
        return root
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorder.reverse()
        d = {v:i for i,v in enumerate(inorder)}
        return self.build(preorder, d, 0, len(preorder)-1)
      
 # WITHOUT USING DICTIONARY ( SLOWER )
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            index = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[index])
            root.left = self.buildTree(preorder, inorder[0:index])
            root.right = self.buildTree(preorder, inorder[index+1:])
            return root
