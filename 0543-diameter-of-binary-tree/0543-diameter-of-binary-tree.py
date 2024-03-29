# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        global cmax
        cmax = 0
        def traverse(root):
            global cmax
            if not root:
                return 0
            lh = traverse(root.left)
            rh = traverse(root.right)
            cmax = max(cmax, lh+rh)
            return max(lh,rh)+1
        
        traverse(root)
        return cmax