from typing import List

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.components = n

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            elif self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_i] = root_j
                self.rank[root_j] += 1
            self.components -= 1
            return True
        return False

class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        # Separate edges into mandatory and optional
        mandatory_edges = []
        optional_edges = []
        
        for u, v, s, must in edges:
            if must == 1:
                mandatory_edges.append((u, v, s))
            else:
                optional_edges.append((u, v, s))
        
        # Sort optional edges in descending order of strength.
        # This allows us to process potentially "zero-cost" edges (s >= S) first
        # during the check, and stop early for weak edges.
        optional_edges.sort(key=lambda x: x[2], reverse=True)
        
        # Helper function to check if a stability of S is achievable
        def check(S: int) -> bool:
            dsu = DSU(n)
            
            # 1. Process Mandatory Edges
            # All mandatory edges must be included. If any has strength < S, it's impossible.
            # Also, mandatory edges must not form a cycle.
            for u, v, s in mandatory_edges:
                if s < S:
                    return False
                if not dsu.union(u, v):
                    return False # Cycle detected among mandatory edges
            
            # 2. Process Optional Edges
            upgrades_used = 0
            
            for u, v, s in optional_edges:
                if s >= S:
                    # The edge already satisfies the stability S.
                    # Use it if it connects two components (greedy approach for spanning tree).
                    dsu.union(u, v)
                elif s * 2 >= S:
                    # The edge can satisfy stability S if upgraded.
                    # Cost is 1 upgrade. We use it only if necessary to connect components.
                    # We stop if we run out of upgrades.
                    if upgrades_used == k:
                        break
                    
                    if dsu.find(u) != dsu.find(v):
                        dsu.union(u, v)
                        upgrades_used += 1
                else:
                    # s * 2 < S: Even with upgrade, this edge is not strong enough.
                    # Since edges are sorted by strength descending, all subsequent edges
                    # will also fail this condition.
                    break
            
            # Check if all nodes are connected
            return dsu.components == 1

        # If stability 1 is not possible, no spanning tree exists (either mandatory edges
        # form a cycle, or graph is disconnected).
        if not check(1):
            return -1
        
        # Binary Search for the maximum stability
        # Range: 1 to 2 * 10^5 (max possible strength after upgrade is 2 * 10^5)
        low = 1
        high = 200000
        ans = 1
        
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
                
        return ans