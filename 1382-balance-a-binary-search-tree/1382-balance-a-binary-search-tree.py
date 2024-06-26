# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        inarr = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            inarr.append(root.val)
            inorder(root.right)
        
        inorder(root)
        print(root)
        
        def createBST(arr, start, end):
            if start>end:
                return None
            mid = (start+end)//2
            root = TreeNode(inarr[mid])
            root.left = createBST(arr, start, mid-1)
            root.right = createBST(arr, mid+1, end)
            return root
        
        return createBST(inarr, 0, len(inarr)-1)     