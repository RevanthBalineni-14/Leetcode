class Solution(object):
    def amountOfTime(self, root, start):
        """
        :type root: Optional[TreeNode]
        :type start: int
        :rtype: int
        """
        res = [0]  # Use a list to make 'res' mutable
        ct = [0]   # Use a list to make 'ct' mutable

        def depth(root):
            if not root:
                return 0
            return max(depth(root.left), depth(root.right)) + 1

        def find(root):
            if not root:
                return False

            if root.val == start:
                res[0] = max(depth(root.left), depth(root.right))
                return True

            if find(root.left):
                ct[0] += 1
                res[0] = max(res[0], ct[0] + depth(root.right))
                return True

            if find(root.right):
                ct[0] += 1
                res[0] = max(res[0], ct[0] + depth(root.left))
                return True

            return False

        find(root)
        return res[0]
