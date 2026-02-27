from collections import deque

class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        start_zeros = s.count('0')
        if start_zeros == 0:
            return 0
        
        # parent[i] points to the next unvisited number >= i with the same parity.
        # We add 2 to the range to handle boundary logic easily.
        parent = list(range(n + 2))
        
        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]

        queue = deque([(start_zeros, 0)])
        # Mark the starting state as "visited" by pointing it to the next available parity
        parent[start_zeros] = find(start_zeros + 2) if start_zeros + 2 <= n + 1 else n + 1
        
        while queue:
            cur_z, steps = queue.popleft()
            
            # Standard boundary logic for flipping k bits
            min_x = max(0, k - (n - cur_z))
            max_x = min(cur_z, k)
            
            # Possible range of new zero-counts
            lower_z = cur_z + k - 2 * max_x
            upper_z = cur_z + k - 2 * min_x
            
            # Use the 'find' function to jump directly to the next unvisited zero-count
            curr = find(lower_z)
            while curr <= upper_z:
                if curr == 0:
                    return steps + 1
                
                queue.append((curr, steps + 1))
                
                # Mark current as visited: point it to the next available number of same parity
                next_val = find(curr + 2) if curr + 2 <= n + 1 else n + 1
                parent[curr] = next_val
                curr = next_val
                
        return -1