# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        
        def dfs(curr, root):
            if not curr:
                return True
            
            if not root or curr.val != root.val:
                return False
            
            return dfs(curr.next, root.left) or dfs(curr.next, root.right)
            
        
        d = deque()
        d.append(root)
        
        while d:
            curr = d.popleft()
            if curr.val == head.val and dfs(head, curr):
                return True
            
            if curr.left:
                d.append(curr.left)
                
            if curr.right:
                d.append(curr.right)
                
        return False