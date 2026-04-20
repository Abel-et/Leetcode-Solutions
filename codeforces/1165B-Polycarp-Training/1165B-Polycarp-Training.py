n = int(input())
arr = list(map(int,input().split()))
arr.sort()

day = 1

for contest in arr:
  if contest >= day:
    day +=1
print(day-1)