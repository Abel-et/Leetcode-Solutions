class Solution:
    def countSubmatrices(self, grid: list[list[int]], k: int) -> int:
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        
        # We'll use the grid itself to store the prefix sums to save space
        for r in range(rows):
            for c in range(cols):
                # Add the sum from the left cell
                if c > 0:
                    grid[r][c] += grid[r][c-1]
                
                # Add the sum from the top cell
                if r > 0:
                    grid[r][c] += grid[r-1][c]
                
                # Subtract the diagonal (top-left) because it was added twice
                if r > 0 and c > 0:
                    grid[r][c] -= grid[r-1][c-1]
                
                # Check if the current submatrix sum is within the limit
                if grid[r][c] <= k:
                    count += 1
                else:
                    # Since values are non-negative, if grid[r][c] > k, 
                    # all larger submatrices in this row will also be > k.
                    break 
                    
        return count
