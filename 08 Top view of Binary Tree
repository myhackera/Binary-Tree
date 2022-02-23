#User function Template for python3

# Tree Node
# class Node:
#     def __init__(self, val):
#         self.right = None
#         self.data = val
#         self.left = None

class Solution:
    def top(self, root, w, h, d):
        if root is None:
            return 
        if w not in d:
            d[w] = [root.data, h]
        elif d[w][1] > h:
            d[w] = [root.data, h]
        self.top(root.left, w-1, h+1, d)
        self.top(root.right, w+1, h+1, d)
        
        
    def topView(self,root):
        d = {}
        ret = []
        w = h = 0
        self.top(root, w, h, d)
        for val in sorted(d.keys()):
            ret.append(d[val][0])
        return ret
