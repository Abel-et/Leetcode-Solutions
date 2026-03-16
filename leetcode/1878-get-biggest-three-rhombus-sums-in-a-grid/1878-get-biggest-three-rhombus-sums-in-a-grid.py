import heapq

class Solution:
    def getBiggestThree(self, grid: list[list[int]]) -> list[int]:
        m, n = len(grid), len(grid[0])
        # Use a set to keep track of unique sums
        sums = set()
        
        for r in range(m):
            for c in range(n):
                # Every single cell is a rhombus of size 0
                sums.add(grid[r][c])
                
                # Try all possible sizes (k) for a rhombus centered at (r, c)
                # k is the distance from the top corner to the center
                for k in range(1, 50):
                    # Check if the four corners of the rhombus are within bounds
                    # Corners: Top (r-k, c), Bottom (r+k, c), Left (r, c-k), Right (r, c+k)
                    if r - k < 0 or r + k >= m or c - k < 0 or c + k >= n:
                        break
                    
                    current_sum = 0
                    # Traverse the 4 edges of the rhombus
                    # Top corner to Right corner
                    for i in range(k):
                        current_sum += grid[r - k + i][c + i]
                    # Right corner to Bottom corner
                    for i in range(k):
                        current_sum += grid[r + i][c + k - i]
                    # Bottom corner to Left corner
                    for i in range(k):
                        current_sum += grid[r + k - i][c - i]
                    # Left corner to Top corner
                    for i in range(k):
                        current_sum += grid[r - i][c - k + i]
                        
                    sums.add(current_sum)
        
        # Return the top 3 distinct sums in descending order
        return sorted(list(sums), reverse=True)[:3]