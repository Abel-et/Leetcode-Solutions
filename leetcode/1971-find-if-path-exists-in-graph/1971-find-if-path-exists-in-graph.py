from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # create a graph 
        graph = defaultdict(list)

        for node, edge in edges:
            graph[node].append(edge)
            graph[edge].append(node)

        # creating stack for instead of callstack and set to put visited node
        stack = [ source]
        visited = set([source])

        while stack:
            node = stack.pop()

            if node == destination:
                return True
            
            visited.add(node)

            for neighbor in  graph[node]:
                if neighbor  not in visited:
                    stack.append(neighbor)
                    visited.add(neighbor)
        return False
        