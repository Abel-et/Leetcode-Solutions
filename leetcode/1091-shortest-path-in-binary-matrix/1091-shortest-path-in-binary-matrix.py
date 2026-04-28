
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # Rule to implement:
            #  all the visited cell of the path are 0 
            # 8 direction 4 diagonals and 4 cross

        # condition to return first
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return - 1
        
        queue = deque()
        visited = set()
        visited.add((0,0))
        dir = [
            (0,1),(1,0),(-1,0),(0,-1),
            (1,1),(-1,1),(1,-1),(-1,-1)
        ]

        # start with the first row, col , distants
        queue.append((0,0,1))
        while queue:
            row , col , dist = queue.popleft()
            if row == n-1 and col == n-1:
                return dist
            
            for dr , dc in dir:
                nr = row + dr
                nc = col + dc
                if 0 <= nr < n and 0 <= nc < n  :
                    if   grid[nr][nc] == 0 and (nr, nc) not in visited:
                        visited.add((nr,nc))
                        queue.append((nr,nc,dist+1))
        return -1