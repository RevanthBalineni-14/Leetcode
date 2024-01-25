class Solution(object):
    def pseudoPalindromicPaths(self, root):
        def dfs(node, path_count):
            if not node:
                return 0
            
            path_count[node.val] += 1
            
            if not node.left and not node.right:
                odd_count = sum(count % 2 for count in path_count.values())
                return 1 if odd_count <= 1 else 0
            
            left_count = dfs(node.left, path_count.copy())
            right_count = dfs(node.right, path_count.copy())
            
            return left_count + right_count
        
        initial_path_count = {digit: 0 for digit in range(1, 10)}
        return dfs(root, initial_path_count)