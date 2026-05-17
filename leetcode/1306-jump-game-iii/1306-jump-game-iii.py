class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        q = deque()
        q.append([arr[start],start])
        seen = set()
        seen.add(start)

        while q : 
            value , index = q.popleft()

            left , right = index - value , index + value

            if value == 0:
                return True
            
            if left > -1 and left not in seen:
                q.append([arr[left], left])
                seen.add(left)

            if right < len(arr) and right not in seen:
                q.append([arr[right],right])
                seen.add(right)

        return False


            