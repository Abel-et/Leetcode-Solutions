class Solution:
    def largestSubmatrix(self, matrix: list[list[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        max_area = 0
        
        for r in range(rows):
            for c in range(cols):
                # Update heights: if 1, add to the height of the column above it
                if matrix[r][c] != 0 and r > 0:
                    matrix[r][c] += matrix[r-1][c]
            
            # Sort the current row's heights in descending order to group tall columns
            curr_row = sorted(matrix[r], reverse=True)
            
            # Calculate area for each potential width (i + 1)
            for i in range(cols):
                max_area = max(max_area, curr_row[i] * (i + 1))
                
        return max_area
