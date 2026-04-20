from collections import Counter
test = int(input())

for _ in range(test):
  n,k = map(int,input().split())
  a = list(map(int,input().split()))
  
  needs = []
  for x in a:
    r = x%k
    if r!=0:
      needs.append((k-r)%k)
  
  if not needs:
    print(0)
    continue
  
  cnt = Counter(needs)
  max_x = 0
  
  for r,c in cnt.items():
    last_x = r + (c-1)*k
    max_x = max(max_x,last_x)
  
  print(max_x+1)