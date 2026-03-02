class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        trailing_zeros = []
        
        # Step 1: Pre-calculate trailing zeros for each row
        for row in grid:
            count = 0
            for i in range(n - 1, -1, -1):
                if row[i] == 0:
                    count += 1
                else:
                    break
            trailing_zeros.append(count)
        
        res = 0
        # Step 2: Greedy approach to find the first row satisfying the condition
        for i in range(n):
            # Row at index i needs at least (n - 1 - i) trailing zeros
            target = n - 1 - i
            found = False
            
            for j in range(i, n):
                if trailing_zeros[j] >= target:
                    # Found a row! Move it to index i using adjacent swaps
                    res += (j - i)
                    # Remove the row from current position and insert it at i
                    # This simulates swapping adjacent rows
                    row_to_move = trailing_zeros.pop(j)
                    trailing_zeros.insert(i, row_to_move)
                    found = True
                    break
            
            if not found:
                return -1
                
        return res