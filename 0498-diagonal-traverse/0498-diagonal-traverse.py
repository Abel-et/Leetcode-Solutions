class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        
        result = []
        row ,col = 0, 0
        direction =  1
        m,n = len(mat), len(mat[0])

        for _ in range(m*n):
            result.append(mat[row][col])

            if direction == 1:
                if col == n-1:
                    row +=1
                    direction = -1
                elif row == 0:
                    col +=1
                    direction  = -1
                else:
                    row -=1
                    col +=1
            else:
                if row == m-1:
                    col +=1
                    direction =1
                elif col == 0:
                    row +=1
                    direction = 1
                else :
                    row +=1
                    col -=1
        return result