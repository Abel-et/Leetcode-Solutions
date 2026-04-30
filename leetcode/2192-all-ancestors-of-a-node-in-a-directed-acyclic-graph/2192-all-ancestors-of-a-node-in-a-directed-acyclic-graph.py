class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # using topological sort 

        # build directed graph  
        graph = [[] for _ in range(n)]
        indegree = [0 for _ in range(n)]

        for form , to in edges:
            graph[form].append(to)
            indegree[to] += 1

        # create a deque as store the source nodes 
        q = deque(i for i in range(n) if indegree[i] == 0)

        # create an result 2d arr to put the final result an parten nodes 
        ans = [[] for _  in range(n)]

        while q:
            node = q.popleft()

            for element in graph[node]:
                # for every edge of the current node append the node value into ans of edges element
                ans[element].append(node)
                
                # appending anscestor node which are the parten of current node
                if ans[node] != []:
                    for i in ans[node]:
                        if i not in ans[element]:
                            ans[element].append(i)
                ans[element].sort()

                indegree[element] -= 1
                if indegree[element] == 0:
                    q.append(element)
        return ans
            
        

        
