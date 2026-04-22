from collections import defaultdict
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = [[False for i in range(len(grid[0]))] for j in range(len(grid)) ]
        row, col = len(grid), len(grid[0])
        direction = [(0,1),(0,-1),(1,0),(-1,0)]

        def inbound(row, col):
            return (0<= row < len(grid)) and (0<= col < len(grid[0]))

        def dfs(grid , visited,row, col):
            visited[row][col] = True
            perimeter = 0

            for row_c , col_c in direction:
                new_r = row + row_c
                new_c = col + col_c

                if not inbound(new_r, new_c) or grid[new_r][new_c] == 0:
                    perimeter += 1
                elif inbound(new_r, new_c) and not visited[new_r][new_c]:
                    perimeter += dfs(grid, visited, new_r, new_c)
            return perimeter
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    return dfs(grid, visited, r ,c)
        return 0