class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_length = len(matrix)
        col_length = len(matrix[0])

        # transposing matrix
        for row in range(row_length):
            for col in range(row, col_length):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
        
        # now reversting each row of matrix
        for row in range(row_length):
            matrix[row].reverse()