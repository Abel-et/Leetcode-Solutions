n, k = map(int , input().split())
    

a = list(map(int, input().split()))
    
  
if k == 1:
    print(a[n-1] - a[0])
else:
  
  diffs = []
  for i in range(n - 1):
      diffs.append(a[i+1] - a[i])

  diffs.sort(reverse=True)
      
  total_cost = a[n-1] - a[0]
      
  total_cost -= sum(diffs[:k-1])
      
  print(total_cost)