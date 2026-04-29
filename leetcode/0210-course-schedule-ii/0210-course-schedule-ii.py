class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[]for _ in range(numCourses)]
        q = deque()
        comming = [0 for _ in range(numCourses)]
        
        
        for course , pre in prerequisites:
            graph[pre].append(course)
            comming[course] += 1

        for edge in range(len(comming)):
            if comming[edge] == 0:
                q.append(edge)
        order = []

        while q :
            course = q.popleft()
            order.append(course)

            for c in graph[course]:
                comming[c] -= 1

                if comming[c] == 0:
                    q.append(c)
        return order if len(order) == numCourses else []
    
