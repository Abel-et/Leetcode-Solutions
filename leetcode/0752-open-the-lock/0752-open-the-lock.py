class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1

        # put the inital starting point and trun into deque
        q = deque()
        q.append(['0000',0])
        visited = set(deadends)

        def childern(lock):
            result = []
            for i in range(4):
                digit = str((int(lock[i])+1 ) % 10)
                result.append(lock[:i] + digit + lock[i+1:])
                digit2 = str((int(lock[i]) - 1 + 10)% 10)
                result.append(lock[:i] + digit2 + lock[i+1:])
            print(result)
            return result

        while q : 
            lock , turn = q.popleft()

            if lock == target:
                return turn

            for child in childern(lock):
                if child  not in visited:
                    visited.add(child)
                    q.append([child,turn + 1])
        return -1