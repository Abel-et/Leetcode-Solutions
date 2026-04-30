import sys
import heapq

input = sys.stdin.readline

n = int(input())
names = [input().strip() for _ in range(n)]

# graph[u] = set of letters that must come after u
graph = [set() for _ in range(26)]
indegree = [0] * 26

# Build constraints from adjacent words
for i in range(n - 1):
    a = names[i]
    b = names[i + 1]

    min_len = min(len(a), len(b))
    found = False

    for j in range(min_len):
        if a[j] != b[j]:
            u = ord(a[j]) - ord('a')
            v = ord(b[j]) - ord('a')

            # Add edge only once
            if v not in graph[u]:
                graph[u].add(v)
                indegree[v] += 1

            found = True
            break

    # Prefix case: "abcd" before "ab" is impossible
    if not found and len(a) > len(b):
        print("Impossible")
        sys.exit()

# Topological sort with min-heap
heap = []
for i in range(26):
    if indegree[i] == 0:
        heapq.heappush(heap, i)

answer = []

while heap:
    u = heapq.heappop(heap)
    answer.append(chr(u + ord('a')))

    for v in graph[u]:
        indegree[v] -= 1
        if indegree[v] == 0:
            heapq.heappush(heap, v)

# If not all letters were used, there is a cycle
if len(answer) != 26:
    print("Impossible")
else:
    print("".join(answer))