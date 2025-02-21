# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:
    def refill(self, root: Optional[TreeNode], parentValue: int, isLeft: bool):
        if not root:
            return 

        if parentValue == -1:
            self.res.add(0)
            self.refill(root.left, 0, True)
            self.refill(root.right, 0, False)
            return
        
        cval = 2*parentValue + (1 if isLeft else 2)
        self.res.add(cval)
        self.refill(root.left, cval, True)
        self.refill(root.right, cval, False)


    def __init__(self, root: Optional[TreeNode]):
        self.res = set()
        self.refill(root, -1, True)
        print(self.res)


    def find(self, target: int) -> bool:
        if target in self.res:
            return True 
        else:
            return False


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)