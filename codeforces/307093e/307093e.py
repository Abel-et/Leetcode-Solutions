from collections import defaultdict

n, k = map(int, input().split())
a = list(map(int, input().split()))

count = defaultdict(int)
left = 0
distinct = 0
ans = 0

for right in range(n):
    if count[a[right]] == 0:
        distinct += 1
    count[a[right]] += 1

    while distinct > k:
        count[a[left]] -= 1
        if count[a[left]] == 0:
            distinct -= 1
        left += 1

    ans += right - left + 1

print(ans)