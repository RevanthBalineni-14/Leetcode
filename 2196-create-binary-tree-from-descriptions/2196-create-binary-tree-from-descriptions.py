# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        mydic = {}
        ch = set()
        for i in descriptions:
            p = i[0]
            c = i[1]
            il = i[2]
            ch.add(c)
            if p in mydic.keys():
                crt = mydic[p]
            else:
                crt = TreeNode(p)
            
            if il==1:
                crt.left = mydic[c] if c in mydic.keys() else TreeNode(c)
                mydic[c] = crt.left
            else:
                crt.right = mydic[c] if c in mydic.keys() else TreeNode(c)
                mydic[c] = crt.right
            
            mydic[p] = crt
            
        root = 0
        for i in descriptions:
            if i[0] not in ch:
                root = i[0]
        
        return mydic[root]