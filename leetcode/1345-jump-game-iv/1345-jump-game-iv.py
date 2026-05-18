from typing import List

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)

        if n <= 1:
            return 0 
            
        # Group indices by their values
        graph = {}
        for i, val in enumerate(arr):
            if val not in graph:
                graph[val] = []
            graph[val].append(i)
            
        curs = [0]
        visited = {0}
        step = 0

        while curs:
            next_level = []

            for node in curs:
                # FIX: Check if the current node is the destination
                if node == n - 1:
                    return step
                
                # Add jumps to indices with the same value
                if arr[node] in graph:
                    for child in graph[arr[node]]:
                        if child not in visited:
                            visited.add(child)
                            next_level.append(child)
                    # OPTIMIZATION: Clear to prevent redundant lookups
                    del graph[arr[node]]

                # Add standard adjacent moves
                for child in [node - 1, node + 1]:
                    if 0 <= child < n and child not in visited:
                        visited.add(child)
                        next_level.append(child)
                        
            curs = next_level
            step += 1
            
        return -1
