class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        
        m, n = len(grid), len(grid[0])
        total_sum = sum(sum(row) for row in grid)
        
        # If sum is odd, equal partition is impossible
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2
        
        # Check horizontal cuts (row by row)
        row_acc = 0
        for i in range(m - 1): # m-1 ensures non-empty bottom section
            row_acc += sum(grid[i])
            if row_acc == target:
                return True
                
        # Check vertical cuts (column by column)
        col_sums = [sum(grid[i][j] for i in range(m)) for j in range(n)]
        col_acc = 0
        for j in range(n - 1): # n-1 ensures non-empty right section
            col_acc += col_sums[j]
            if col_acc == target:
                return True
                
        return False
