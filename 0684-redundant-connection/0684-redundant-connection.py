class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        root = list(range(len(edges) + 1))

        def find(node):
            if root[node] != node:
                root[node] = find(root[node])
            return root[node]
        
        for node1, node2 in edges:
            root1, root2 = find(node1), find(node2)

            if root1 == root2:
                return [node1, node2]
            
            root[root1] = root2