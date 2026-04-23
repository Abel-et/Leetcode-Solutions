# the question need after t second change the boys position t step into back
n , t = map(int, input().split())

# the queue
s = list(input())

for _ in range(t):
    i = 0
    
    while i < n-1:
        if s[i] == 'B' and s[i+1] =='G':
            s[i], s[i+1] = s[i+1] , s[i]
            i +=2
        else:
            i += 1 
            
            
print(''.join(s))