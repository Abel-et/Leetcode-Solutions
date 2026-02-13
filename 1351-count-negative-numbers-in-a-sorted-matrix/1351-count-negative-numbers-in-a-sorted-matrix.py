from collections import Counter
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        c = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] < 0:
                    c+=1
        return c

       
        