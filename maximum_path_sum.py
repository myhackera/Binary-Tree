# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.answer = float('-inf')
        
        def postorder_dfs(node):
            if not node:
                return 0
            left = max(0, postorder_dfs(node.left))
            right = max(0, postorder_dfs(node.right))
            self.answer = max(self.answer, left + right + node.val)
            return max(left, right) + node.val
        postorder_dfs(root)
        return self.answer
