n , m = map(int , input().split())
arr1 = list(map(int , input().split()))
arr2 = list(map(int , input().split()))

# objective
#   for each element of arr2 
#    find how many numbers are strictly less than form arr1

ans = []
j = 0
# using for while combo two pointer approach
for i in range(len(arr2)):
    
    # while first array is less than second arr and pointer less than the length of first arr
    while arr1[j] < arr2[i] and j < n-1:
        # update the pointer
        j += 1
        
    # check the pointer is found at the last index , and first arr of last element is less than the current second arr element
    if j == n-1 and arr1[j] < arr2[i] :
        ans.append(n)
    else:
        ans.append(j)
print(*ans)