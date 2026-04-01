class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:

        n = len(positions)
        # 1. Create indexed list to track original order and sort by position
        # indices = [0, 1, 2, ..., n-1]
        indices = sorted(range(n), key=lambda i: positions[i])
        
        stack = [] # Stores indices of robots moving to the RIGHT ('R')
        
        for i in indices:
            if directions[i] == 'R':
                stack.append(i)
            else:
                # 2. Collision logic: Current robot is moving LEFT ('L')
                # It will collide with any 'R' robot currently in the stack
                while stack and healths[i] > 0:
                    top = stack[-1]
                    
                    if healths[top] > healths[i]:
                        # 'R' robot wins: loses 1 HP, 'L' robot destroyed
                        healths[top] -= 1
                        healths[i] = 0
                    elif healths[top] < healths[i]:
                        # 'L' robot wins: loses 1 HP, 'R' robot popped from stack
                        healths[i] -= 1
                        healths[top] = 0
                        stack.pop()
                    else:
                        # Tie: Both are destroyed
                        healths[i] = 0
                        healths[top] = 0
                        stack.pop()
        
        # 3. Filter healths > 0 to get only survivors in original index order
        return [h for h in healths if h > 0]
