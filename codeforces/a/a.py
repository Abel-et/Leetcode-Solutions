import sys
from collections import deque

def solve():
    # Use fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    
    # Handle the base case for a single node
    if n == 1:
        print(0)
        return

    # Build adjacency list using a list of lists
    adj = [[] for _ in range(n + 1)]
    idx = 1
    for _ in range(n - 1):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2

    def get_farthest(start_node):
        # BFS to find the farthest node and its distance
        distances = [-1] * (n + 1)
        distances[start_node] = 0
        queue = deque([start_node])
        
        farthest_node = start_node
        max_dist = 0
        
        while queue:
            u = queue.popleft()
            
            if distances[u] > max_dist:
                max_dist = distances[u]
                farthest_node = u
                
            for v in adj[u]:
                if distances[v] == -1:
                    distances[v] = distances[u] + 1
                    queue.append(v)
                    
        return farthest_node, max_dist

    # Step 1: Find one end of the diameter
    u, _ = get_farthest(1)
    
    # Step 2: Find the actual diameter from that end
    v, diameter = get_farthest(u)

    # Step 3: Calculate circumference (diameter * pi, where pi = 3)
    print(diameter * 3)

if __name__ == "__main__":
    solve()