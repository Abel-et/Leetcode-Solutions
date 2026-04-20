import sys

def solve():
    # Fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    pointer = 1
    
    results = []
    for _ in range(t):
        n = int(input_data[pointer])
        p = list(map(int, input_data[pointer + 1 : pointer + 1 + n]))
        pointer += 1 + n
        
        # We always keep the first element
        res = [p[0]]
        
        # Check every element from the second to the second-to-last
        for i in range(1, n - 1):
            # Check if p[i] is NOT a middle point in a monotonic sequence
            # If it IS a peak or a valley, we must keep it
            if not ((p[i-1] < p[i] < p[i+1]) or (p[i-1] > p[i] > p[i+1])):
                res.append(p[i])
        
        # We always keep the last element
        res.append(p[-1])
        
        # Store results to print all at once
        results.append(f"{len(res)}")
        results.append(" ".join(map(str, res)))
    
    print("\n".join(results))

if __name__ == "__main__":
    solve()