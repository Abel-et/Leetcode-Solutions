class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix[0])
        
        
        # applay binary search algortihm 
        def binary_search(row):
            left , right = 0 , len(row) -1

            while left <= right:
                mid = (left + right)//2

                if row[mid] == target:
                    return True
                elif row[mid] > target:
                    right = mid -1
                else:
                    left = mid +1
            return False
        
        for row in matrix:
            if row[m-1] >= target and row[0] <= target:
                return binary_search(row)
        return False

        # in place less time O(mlogn )