import sys

def solve():
    # Use fast I/O
    input = sys.stdin.read().split()
    if not input:
        return
    
    n = int(input[0])
    k = int(input[1])
    q = int(input[2])
    
    MAX_TEMP = 200000
    diff = [0] * (MAX_TEMP + 2)
    
    # Step 1: Difference Array for recipes
    idx = 3
    for _ in range(n):
        l = int(input[idx])
        r = int(input[idx+1])
        diff[l] += 1
        diff[r + 1] -= 1
        idx += 2
        
    # Step 2: Prefix sum to find admissible temps
    admissible_count = [0] * (MAX_TEMP + 1)
    current_recipes = 0
    for i in range(1, MAX_TEMP + 1):
        current_recipes += diff[i]
        if current_recipes >= k:
            admissible_count[i] = 1
        else:
            admissible_count[i] = 0
            
    # Step 3: Prefix sum of admissible temps for range queries
    pref_sum = [0] * (MAX_TEMP + 1)
    for i in range(1, MAX_TEMP + 1):
        pref_sum[i] = pref_sum[i-1] + admissible_count[i]
        
    # Step 4: Process Queries
    results = []
    for _ in range(q):
        a = int(input[idx])
        b = int(input[idx+1])
        results.append(str(pref_sum[b] - pref_sum[a-1]))
        idx += 2
        
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()