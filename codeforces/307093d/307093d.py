n ,  s = map(int, input().split())

arr = list(map(int, input().split()))

current_sum = 0
segment = 0
left = 0
for i in range(n):
    current_sum += arr[i]
    
    while current_sum > s:
        segment += (n-i)
        current_sum -= arr[left]
        left +=1
        
print(segment)