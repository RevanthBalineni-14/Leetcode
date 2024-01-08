# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        res = []
        def recurse(root):
            if not root:
                return
            recurse(root.left)
            res.append(root.val)
            recurse(root.right)
        
        recurse(root)
        return sum(res[res.index(low):res.index(high)+1])