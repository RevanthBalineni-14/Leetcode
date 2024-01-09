# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        res = []
        def recurse(root):
            if not root:
                return
            if not root.left and not root.right:
                res.append(root.val)
                return
            recurse(root.left)
            recurse(root.right)
        
        recurse(root1)
        res1 = res
        res = []
        recurse(root2)
        res2 = res
        if res1 == res2:
            return True
        else:
            return False