# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        self.mydic = {}
        def traverse(self, root, level):
            self.mydic[level] = self.mydic.get(level, 0) + root.val
            if root.left is not None:
                traverse(self, root.left, level + 1)
            
            if root.right is not None:
                traverse(self, root.right, level + 1)
        
        traverse(self, root, 0)
        
        heap = []
        for i in self.mydic.keys():
            if len(heap)<k:
                heapq.heappush(heap, self.mydic[i])
            else:
                if heap[0]<self.mydic[i]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, self.mydic[i])
                    
        if len(heap)<k:
            return -1
        else:
            return heap[0]