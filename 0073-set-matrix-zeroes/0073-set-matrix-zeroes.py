class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_index = set()
        col_index = set()
        num_row = len(matrix)
        num_col = len(matrix[0])


        def index_tracker(row,col):
            row_part = set()
            col_part = set()

            for r in range(num_col):
                row_part.add((row,r))

            for c in range(num_row):
                col_part.add((c,col))
            return [row_part, col_part]
   

        for row in range(num_row):
            for col in range(num_col):
                if matrix[row][col] == 0:
                    indices = index_tracker(row,col)
                    row_index.update((index) for index in indices[0])
                    col_index.update(index for index in indices[1])
        
        for r in row_index:
            row = r[0]
            col = r[1]
            matrix[row][col] = 0
        
        for c in col_index:
            col = c[1]
            row = c[0]
            matrix[row][col] = 0
        
       
            
           




      