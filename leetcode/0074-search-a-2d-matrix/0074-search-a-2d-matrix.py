class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # convet the 2D matrix into on 1D matrix
        mat = []
        for matr in matrix:
            mat.extend(matr)
        
        # applay binary search algortihm 
        left , right = 0 , len(mat) -1

        while left <= right:
            mid = (left + right)//2

            if mat[mid] == target:
                return True
            elif mat[mid] > target:
                right = mid -1
            else:
                left = mid +1
        return False