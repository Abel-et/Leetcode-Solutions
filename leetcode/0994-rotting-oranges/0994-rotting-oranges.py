class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows =  len(grid)
        cols = len(grid[0])
        minute = 0
        fresh = 0
        queue = deque()
        
        # add all rotten orange into the queue and counting how many fresh orange are there
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row,col))
                elif grid[row][col] == 1:
                    fresh += 1
        #  4 direction of rotten orange adjacents
        dir = [(0, 1), (1, 0),(-1,0),(0,-1)]

        # now use bfs multis sources temaplate
        while queue and fresh > 0 :
            # traversing every node of each level
            for _ in range(len(queue)):
                row , col = queue.popleft()

                for dr , dc in dir:
                    new_row = row + dr
                    new_col = col + dc
                    if 0 <= new_row < rows and 0 <= new_col < cols:
                        if grid[new_row][new_col] == 1:
                            grid[new_row][new_col] = 2
                            fresh -= 1 
                            queue.append((new_row,new_col))
            minute += 1
        return minute if fresh == 0 else -1
