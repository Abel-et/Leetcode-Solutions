from collections import defaultdict
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        RED, BLUE = 0, 1
        queue = deque()

        # build directed graph
        redgraph = defaultdict(list)
        bluegraph = defaultdict(list)

        for u, v in redEdges:
            redgraph[u].append(v)

        for i , j in blueEdges:
            bluegraph[i].append(j)

        distance = [[float('inf')] * 2 for _ in range(n)]
        queue.append((0,RED))
        queue.append((0,BLUE))

        distance[0][RED] = 0
        distance[0][BLUE] = 0

        while queue:
            node , color = queue.popleft()
            
            if color == RED:
                next_color = BLUE
                nei = redgraph[node]
            else:
                next_color = RED
                nei = bluegraph[node]

            for neighbor in nei:
                if distance[neighbor][next_color] == float('inf'):
                    distance[neighbor][next_color] = distance[node][color] + 1
                    queue.append((neighbor, next_color))
        ans = []

        for i in range(n):
            best = min(distance[i][BLUE], distance[i][RED])
            ans.append(-1 if best == float('inf') else best)
        return ans
