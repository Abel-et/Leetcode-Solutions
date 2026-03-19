class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        # dpX[i][j] stores count of 'X' from (0,0) to (i-1, j-1)
        dpX = [[0] * (n + 1) for _ in range(m + 1)]
        dpY = [[0] * (n + 1) for _ in range(m + 1)]
        ans = 0
        
        for i in range(m):
            for j in range(n):
                # Update prefix sum for X
                valX = 1 if grid[i][j] == 'X' else 0
                dpX[i+1][j+1] = valX + dpX[i][j+1] + dpX[i+1][j] - dpX[i][j]
                
                # Update prefix sum for Y
                valY = 1 if grid[i][j] == 'Y' else 0
                dpY[i+1][j+1] = valY + dpY[i][j+1] + dpY[i+1][j] - dpY[i][j]
                
                # Check conditions
                if dpX[i+1][j+1] > 0 and dpX[i+1][j+1] == dpY[i+1][j+1]:
                    ans += 1
                    
        return ans
