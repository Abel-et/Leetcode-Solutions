class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        q = deque()
        q.append((0,[0]))

        target = len(graph)-1
        ans = []

        while q:
            node , path = q.popleft()

            if node == target:
                ans.append(path)
                continue
            for nei in graph[node]:
                q.append((nei, path + [nei]))
        return ans
        