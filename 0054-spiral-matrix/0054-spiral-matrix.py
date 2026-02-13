class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

       
        spiral = []

        if not matrix or not matrix[0]:
            return []


        top , bottom = 0 , len(matrix)-1
        left, right = 0 , len(matrix[0])-1

        while top <= bottom and left <= right:
            # left to right
            for col in range(left, right + 1):
                spiral.append(matrix[top][col])
            top += 1

            # from top to bottom 
            for row in range(top, bottom + 1):
                spiral.append(matrix[row][right])
            right -=1
           
            # from right to left
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    spiral.append(matrix[bottom][col])
                bottom -= 1
           

            # from bottom to top
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    spiral.append(matrix[row][left])
                left += 1
                
        return spiral


