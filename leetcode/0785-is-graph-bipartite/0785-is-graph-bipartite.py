
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        # -1: Uncolored, 0: Color A, 1: Color B
        colors = [-1] * n

        def dfs(u, color):
            colors[u] = color
            
            for v in graph[u]:
                # If the neighbor isn't colored, color it with the opposite color
                if colors[v] == -1:
                    if not dfs(v, 1 - color):
                        return False
                # If the neighbor has the same color, we found an odd cycle
                elif colors[v] == color:
                    return False
                    
            return True

        # Iterate through all nodes to handle disconnected components
        for i in range(n):
            if colors[i] == -1:
                if not dfs(i, 0):
                    return False
                    
        return True
        