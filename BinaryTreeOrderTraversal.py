# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return 
        res = []
        queue = [root]
        while(queue):
            l = []
            for _ in range(len(queue)):
                l.append(queue[0].val)
                temp = queue.pop(0)
                if temp.left is not None:
                    queue.append(temp.left)
                if temp.right is not None:
                    queue.append(temp.right)
            res.append(l)
        return res
            
