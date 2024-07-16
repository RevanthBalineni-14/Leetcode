# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        def lca(root, start, dest):
            if not root:
                return None
            
            if (root.val == start or root.val == dest):
                return root
            
            l = lca(root.left, start, dest)
            r = lca(root.right, start, dest)
            
            if l and r:
                return root
            
            if l:
                return l
            else:
                return r
        
        def pathf(root, val, path):
            if not root:
                return False
            if root.val == val:
                return True
            
            path.append('L')
            if pathf(root.left, val, path):
                return True
            path.pop()
            
            path.append('R')
            if pathf(root.right, val, path):
                return True
            path.pop()
            
            return False
        
        sp, dp = [], []
        
        lc = lca(root, startValue, destValue)
        pathf(lc, startValue, sp)
        pathf(lc, destValue, dp)
        
        res = 'U' * len(sp)
        res += ''.join(dp)
        
        return res