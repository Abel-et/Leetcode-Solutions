n , m  = map(int,input().split())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

ans = []
i , j = 0 , 0
#  this sorting is use full on quick and merge sort to combine the left and right arr together
while i < n and j < m:
    if arr1[i] > arr2[j]:
        ans.append(arr2[j])
        j += 1
    else:
        ans.append(arr1[i])
        i += 1
ans.extend(arr1[i:])
ans.extend(arr2[j:])
print(*ans)