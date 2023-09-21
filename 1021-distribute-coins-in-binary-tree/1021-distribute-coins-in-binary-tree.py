# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        global total
        total=0 

        def traverse(root):
            if(root==None):
                return 0
            rval=traverse(root.right)
            lval=traverse(root.left)
            global total
            total+=abs(rval)+abs(lval)
                        
            return rval+lval+root.val-1
        
        traverse(root)

        return total
