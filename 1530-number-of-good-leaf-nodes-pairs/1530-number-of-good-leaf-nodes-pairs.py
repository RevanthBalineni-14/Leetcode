# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.res = 0
        
        def recurse(node, dist):
            if not node:
                return [0] * 11
            
            l = recurse(node.left, dist)
            r = recurse(node.right, dist)
            
            crt = [0] * 11
            
            if not node.right and not node.left:
                crt[1] = 1
                return crt
            
            for i in range(11):
                for j in range(11):
                    if i + j <= dist:
                        self.res += l[i] * r[j]
            
            for i in range(10):
                crt[i + 1] += l[i] + r[i]
            
            return crt
            
        recurse(root, distance)
        return self.res
