# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return 
        flag = 0 # For right to left
        res = []
        queue = [root]
        while(queue):
            l = []
            for _ in range(len(queue)):
                l.append(queue[0].val)
                temp = queue.pop(0)
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
            if flag == 1:
                l.reverse()
                res.append(l)
                flag = 0
            else:
                res.append(l)
                flag = 1
        return res
                
                
