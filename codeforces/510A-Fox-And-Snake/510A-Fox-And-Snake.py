n , m = map(int, input().split())

grid = [[] for _ in range(n)]

toggle = True
for i in range(n):
    if i % 2 == 0 :
        for _ in range(m):
            grid[i].append('#')
    else:
        if toggle:
            for _ in range(m-1):
                grid[i].append('.')
            grid[i].append('#')
            toggle = False
        else:
            grid[i].append('#')
            toggle = True
            for _ in range(m-1):
                grid[i].append('.')
        

for g in grid:
    print(''.join(g))