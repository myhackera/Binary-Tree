class Solution(object):
    def verticalTraversalHelper(self, root, row, col):
        if not root:
            return 
        
        
        if row in self.d[col]:
            self.d[col][row].append(root.val)
        else:
            self.d[col][row] = []
            self.d[col][row].append(root.val)
            
        
        self.verticalTraversalHelper(root.left, row+1, col-1)
        self.verticalTraversalHelper(root.right, row+1, col+1)
        
    def verticalTraversal(self, root):
        
        self.d = collections.defaultdict(dict)
        self.verticalTraversalHelper(root, 0, 0)
        
        res = []

        for col in sorted(self.d.keys()):
            r = []
            for row in sorted(self.d[col].keys()):
                for ele in sorted(self.d[col][row]):
                    r.append(ele)
            
            res.append(r)
                
        
        return res
        
