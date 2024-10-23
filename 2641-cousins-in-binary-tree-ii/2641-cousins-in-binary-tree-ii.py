# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.mydic = {}
        def traverse(self, root, level):
            self.mydic[level] = self.mydic.get(level, 0) + root.val
            if root.left is not None:
                traverse(self, root.left, level + 1)
            
            if root.right is not None:
                traverse(self, root.right, level + 1)
        
        traverse(self, root, 0)
        
        def replace_with_sum(self, root, level, prevsum):
            
            if not root:
                return
            crtsum = 0
            if root.left:
                crtsum += root.left.val
            if root.right:
                crtsum += root.right.val
            if level == 0:
                root.val = 0
                replace_with_sum(self, root.left, level+1, crtsum)
                replace_with_sum(self, root.right, level+1, crtsum)
            else:
                root.val = self.mydic[level] - prevsum
                replace_with_sum(self, root.left, level+1, crtsum)
                replace_with_sum(self, root.right, level+1, crtsum)
        
        replace_with_sum(self, root, 0, 0)
        
        return root