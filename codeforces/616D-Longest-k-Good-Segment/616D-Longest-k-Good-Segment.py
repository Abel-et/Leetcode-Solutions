import sys
from collections import defaultdict

def solve():
    # Fast I/O
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    k = int(data[1])
    # Converting to int list immediately
    arr = list(map(int, data[2:]))

    counts = defaultdict(int)
    unique_count = 0
    left = 0
    max_len = -1
    best_l, best_r = 1, 1

    for right in range(n):
        # Add right element to window
        val_r = arr[right]
        if counts[val_r] == 0:
            unique_count += 1
        counts[val_r] += 1
        
        # Shrink window if more than k unique elements
        while unique_count > k:
            val_l = arr[left]
            counts[val_l] -= 1
            if counts[val_l] == 0:
                unique_count -= 1
            left += 1
        
        # Update the longest segment found so far
        current_len = right - left + 1
        if current_len > max_len:
            max_len = current_len
            best_l, best_r = left + 1, right + 1
            
    # Output the 1-based indices
    sys.stdout.write(f"{best_l} {best_r}\n")

if __name__ == "__main__":
    solve()