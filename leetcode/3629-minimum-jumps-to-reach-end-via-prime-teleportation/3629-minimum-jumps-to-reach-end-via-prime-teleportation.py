import collections
class Solution:
    def minJumps(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n == 1: return 0
        
        max_val = max(nums)
        
        # 1. Precompute primes using Sieve
        is_prime = [True] * (max_val + 1)
        is_prime[0] = is_prime[1] = False
        for p in range(2, int(max_val**0.5) + 1):
            if is_prime[p]:
                for i in range(p * p, max_val + 1, p):
                    is_prime[i] = False
        
        # 2. Map primes to indices of their multiples
        # prime_to_indices[p] = list of indices j such that nums[j] % p == 0
        prime_to_indices = collections.defaultdict(list)
        for i, val in enumerate(nums):
            # Find prime factors of each number to build the "backwards" links
            # Optimization: We only care about primes that actually appear in nums
            # as teleportation triggers.
            d = 2
            temp = val
            while d * d <= temp:
                if temp % d == 0:
                    prime_to_indices[d].append(i)
                    while temp % d == 0: temp //= d
                d += 1
            if temp > 1:
                prime_to_indices[temp].append(i)

        # 3. BFS
        queue = collections.deque([(0, 0)]) # (index, distance)
        visited_idx = {0}
        visited_prime = set()
        
        while queue:
            curr_idx, dist = queue.popleft()
            
            if curr_idx == n - 1:
                return dist
                
            # Option 1: Adjacent Steps (Weight 1)
            for neighbor in [curr_idx - 1, curr_idx + 1]:
                if 0 <= neighbor < n and neighbor not in visited_idx:
                    visited_idx.add(neighbor)
                    queue.append((neighbor, dist + 1))
            
            # Option 2: Prime Teleportation (Weight 1)
            val = nums[curr_idx]
            if is_prime[val] and val not in visited_prime:
                visited_prime.add(val)
                for target_idx in prime_to_indices[val]:
                    if target_idx not in visited_idx:
                        visited_idx.add(target_idx)
                        queue.append((target_idx, dist + 1))
                        
        return -1
