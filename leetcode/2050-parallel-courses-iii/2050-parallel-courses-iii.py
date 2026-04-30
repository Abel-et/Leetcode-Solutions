class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        indegree = [0 for _ in range(n+1)]
        graph = [[] for _ in range(n+1)]

        for pre , next in relations:
            graph[pre].append(next)
            indegree[next] += 1

        q = deque()
        finish = [0]*(n+1)
        for degree in range(1,len(indegree)):
            if indegree[degree] == 0:
                q.append(degree)
                finish[degree] = time[degree-1]        
        
        while q:       
            node = q.popleft()
               
            for edge in graph[node]:
                indegree[edge] -= 1
                finish[edge] = max( finish[edge], finish[node] + time[edge-1])
                if indegree[edge] == 0:
                    q.append(edge)
        
        return max(finish)
