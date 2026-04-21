n , s = map(int , input().split())
arr = list(map(int , input().split()))

left , current_sum , segment = 0, 0 , 0

for right in range(len(arr)):
    current_sum += arr[right]

    while current_sum > s:
        current_sum -= arr[left]
        left += 1
        
    segment += (right - left + 1)
print(segment)