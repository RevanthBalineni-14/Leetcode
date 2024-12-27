# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def swaps(self, arr):
            dic = {}
            for pos, i in enumerate(arr):
                dic[i] = pos
            sarr = sorted(arr)
            for i in range(len(sarr)):
                if sarr[i] != arr[i]:
                    pos = dic[sarr[i]]
                    temp = arr[i]
                    arr[i] = arr[pos]
                    arr[pos] = temp
                    
                    dic[temp] = pos
                    self.swaps += 1
        
        def traverse(self, root, level):
            if not root:
                return
            self.mydic[level].append(root.val)
            traverse(self, root.left, level+1)
            traverse(self, root.right, level+1)
        
        self.mydic = defaultdict(list)
        traverse(self, root, 0)
        self.swaps = 0
        for i in self.mydic.keys():
            swaps(self, self.mydic[i])
        
        return self.swaps
                    