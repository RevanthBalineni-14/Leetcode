# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        inarr = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            inarr.append(root.val)
            inorder(root.right)
            
        
        inorder(root)
        self.count = 0
        def converted(self, root):
            if not root:
                return
            converted(self, root.left)
            
            if self.count!=(len(inarr)-1):
                root.val += sum(inarr[(self.count+1):])
            self.count += 1
            
            converted(self, root.right)
            
        converted(self, root)
        return root