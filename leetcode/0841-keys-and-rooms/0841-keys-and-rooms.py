class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        q = deque([0])
        visited= set([0])
        n = len(rooms) 

        while q :
            node = q.popleft()

            for key in rooms[node]:
                if key not in visited:
                    visited.add(key)
                    q.append(key)
        return n == len(visited)

