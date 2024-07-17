# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        st = []
        st.append(root)
        def traverse(root, ele, new_st):
            if not root:
                return False
            if root.val == ele:
                if root.left:
                    new_st.append(root.left)
                if root.right:
                    new_st.append(root.right)
                return True
            
            if traverse(root.left, ele, new_st):
                root.left = None
            
            if traverse(root.right, ele, new_st):
                root.right = None
                
            return False
        
        for i in to_delete:
            new_st = []
            for crt in st:
                if traverse(crt, i, new_st):
                    pass
                else:
                    new_st.append(crt)
            st = new_st
                
        return st