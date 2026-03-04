class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        cnt = 0

        def horizontal(i):
            return True if mat[i].count(1) == 1 else False
        
        def vertical(j):
            size_mat = len(mat)
            selected_col = []
            for i in range(size_mat):
                selected_col.append(mat[i][j])
            
            return True if selected_col.count(1) == 1 else False
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    if vertical(j) and  horizontal(i):
                        cnt +=1
                    else:
                        continue
        return cnt