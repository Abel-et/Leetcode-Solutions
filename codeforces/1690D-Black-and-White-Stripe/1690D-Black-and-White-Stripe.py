# fixed size sliding window problem

for _ in range(int(input())):
    n , k = map(int,input().split())
    colors = input()
    currentW = 0
    
    for i in range(k):
        if colors[i] == 'W':
            currentW +=1
            
    minW = currentW
    for i in range(k , n):
        if colors[i] == 'W':
            currentW += 1
        if colors[i-k] == 'W':
            currentW -= 1
            
        if currentW < minW:
            minW = currentW
    print(minW)