from collections import Counter
import sys

def solve():
    # Read n, left_count, right_count
    n, l, r = map(int, sys.stdin.readline().split())
    colors = list(map(int, sys.stdin.readline().split()))
    
    # Split into Left and Right counters
    left_socks = Counter(colors[:l])
    right_socks = Counter(colors[l:])
    
    # 1. Remove socks that already match (Intersection)
    common = left_socks & right_socks
    left_socks -= common
    right_socks -= common
    
    # Current remaining counts
    l_rem = sum(left_socks.values())
    r_rem = sum(right_socks.values())
    
    # Ensure l_rem is always the "heavier" side for simpler logic
    if l_rem < r_rem:
        left_socks, right_socks = right_socks, left_socks
        l_rem, r_rem = r_rem, l_rem
        
    # 2. We need to move socks from Left to Right to balance them
    # Cost to balance side counts: (l_rem - r_rem) // 2
    diff = l_rem - r_rem
    cost = 0
    
    # 3. Greedy: Fix same-color pairs on the heavy side first
    # This saves us from needing to recolor later
    for color in left_socks:
        if diff <= 0: break
        
        # How many pairs of this color can we flip?
        pairs = left_socks[color] // 2
        can_fix = min(pairs, diff // 2)
        
        cost += can_fix
        diff -= can_fix * 2
        l_rem -= can_fix * 2

    # 4. Final calculation
    # Any remaining 'diff' must be moved (1$ each)
    # Then, all remaining socks are balanced but different colors (1$ per pair)
    cost += diff + (l_rem + r_rem - diff) // 2
    print(cost)

# For multiple test cases
t_str = sys.stdin.readline().strip()
if t_str:
    t = int(t_str)
    for _ in range(t):
        solve()