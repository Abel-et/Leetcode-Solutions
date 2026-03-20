# class Solution:
#     def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
from typing import List

    
class Solution:
    def minAbsDiff(self, grid: list[list[int]], k: int) -> list[list[int]]:
        m, n = len(grid), len(grid[0])
        ans_rows = m - k + 1
        ans_cols = n - k + 1
        ans = [[0] * ans_cols for _ in range(ans_rows)]
        
        for i in range(ans_rows):
            for j in range(ans_cols):
                # 1. Extract all elements in the k x k submatrix
                elements = []
                for r in range(i, i + k):
                    for c in range(j, j + k):
                        elements.append(grid[r][c])
                
                # 2. Get unique values and sort them
                unique_sorted = sorted(list(set(elements)))
                
                # 3. Calculate minimum absolute difference
                if len(unique_sorted) <= 1:
                    ans[i][j] = 0
                else:
                    min_diff = float('inf')
                    for x in range(len(unique_sorted) - 1):
                        diff = abs(unique_sorted[x+1] - unique_sorted[x])
                        if diff < min_diff:
                            min_diff = diff
                    ans[i][j] = min_diff
                    
        return ans
