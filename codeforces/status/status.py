n, s = map(int,input().split())
arr = list(map(int,input().split()))
 
total,curr,left = 0,0,0

for right in range(n):
  curr += arr[right]
  
  while curr > s:
    curr -= arr[left]
    left +=1

  total += (right -left +1)
print(total)