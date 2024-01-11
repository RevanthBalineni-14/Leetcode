# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        cmin, cmax = root.val, root.val
        res = [0]
        def recurse(root, cmin, cmax):
            if not root:
                return
            res[0] = max(res[0], max(abs(cmin-root.val), abs(cmax-root.val)))
            cmin = min(cmin, root.val)
            cmax = max(cmax, root.val)
            recurse(root.left, cmin, cmax)
            recurse(root.right, cmin, cmax)
        recurse(root, cmin, cmax)
        return res[0]