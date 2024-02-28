# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        mydic = {}
        self.cmax = 0  
        def traverse(root, crt):
            if not root:
                return
            if crt>self.cmax:
                mydic[crt] = root.val
                self.cmax = crt
            traverse(root.left, crt+1)
            traverse(root.right, crt+1)
        
        traverse(root, 1)  # Start traversal with initial depth as 1
        return mydic[self.cmax]
