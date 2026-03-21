class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        top = x
        bottom = x + k - 1
        
        while top < bottom:
            # Swap the specific segment [y : y+k] between the two rows
            grid[top][y : y+k], grid[bottom][y : y+k] = \
            grid[bottom][y : y+k], grid[top][y : y+k]
            
            top += 1
            bottom -= 1
            
        return grid