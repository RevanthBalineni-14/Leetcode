from collections import defaultdict
from typing import List

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = defaultdict(list)
        visited = set()

        # Create adjacency list
        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
        
        for i in range(n):
            if i not in adjList:
                adjList[i] = []

        def dfs(node, component):
            stack = [node]
            visited.add(node)
            component_nodes = [node]

            while stack:
                curr = stack.pop()
                for neighbor in adjList[curr]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        component_nodes.append(neighbor)
                        stack.append(neighbor)
            
            return component_nodes

        compIdx = 0
        for node in range(n):
            if node not in visited:
                component_nodes = dfs(node, compIdx)
                # Check if the component is complete
                is_complete = True
                for comp_node in component_nodes:
                    if len(adjList[comp_node]) != len(component_nodes) - 1:
                        is_complete = False
                        break
                if is_complete:
                    compIdx += 1
        
        return compIdx
