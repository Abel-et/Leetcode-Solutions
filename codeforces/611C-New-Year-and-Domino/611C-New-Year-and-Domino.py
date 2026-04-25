import sys

def solve():
    input = sys.stdin.read().split()
    h, w = int(input[0]), int(input[1])
    grid = input[2:2+h]
    q = int(input[2+h])
    queries = input[3+h:]

    # Horizontal and Vertical valid placements
    hor = [[0]*(w+1) for _ in range(h+1)]
    ver = [[0]*(w+1) for _ in range(h+1)]
    
    for i in range(1, h + 1):
        for j in range(1, w + 1):
            if j < w and grid[i-1][j-1] == '.' and grid[i-1][j] == '.':
                hor[i][j] = 1
            if i < h and grid[i-1][j-1] == '.' and grid[i][j-1] == '.':
                ver[i][j] = 1

    # Build Prefix Sums
    prefH = [[0]*(w+1) for _ in range(h+1)]
    prefV = [[0]*(w+1) for _ in range(h+1)]
    for i in range(1, h + 1):
        for j in range(1, w + 1):
            prefH[i][j] = hor[i][j] + prefH[i-1][j] + prefH[i][j-1] - prefH[i-1][j-1]
            prefV[i][j] = ver[i][j] + prefV[i-1][j] + prefV[i][j-1] - prefV[i-1][j-1]

    # Process Queries
    results = []
    for k in range(0, len(queries), 4):
        r1, c1, r2, c2 = map(int, queries[k:k+4])
        
        res = 0
        if c2 > c1: # Horizontal check
            res += prefH[r2][c2-1] - prefH[r1-1][c2-1] - prefH[r2][c1-1] + prefH[r1-1][c1-1]
        if r2 > r1: # Vertical check
            res += prefV[r2-1][c2] - prefV[r2-1][c1-1] - prefV[r1-1][c2] + prefV[r1-1][c1-1]
        results.append(str(res))
    
    sys.stdout.write("\n".join(results) + "\n")

solve()