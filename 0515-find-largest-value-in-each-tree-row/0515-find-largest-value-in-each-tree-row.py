# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        self.mydic = {}
        def traverse(self, root, level):
            if not root:
                return
            if level not in self.mydic.keys():
                self.mydic[level] = root.val
            else:
                self.mydic[level] = max(self.mydic[level], root.val)
            
            traverse(self, root.left, level+1)
            traverse(self, root.right, level+1)
            
        res = []
        traverse(self, root, 1)
        i = 1
        
        while True:
            if i in self.mydic.keys():
                res.append(self.mydic[i])
            else:
                break
            i+=1
        
        return res