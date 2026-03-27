import copy
class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        
        def right_shift(arr):
            last_element = arr.pop()
            arr.insert(0,last_element)
            return arr
        def left_shift(arr):
            first_element = arr.pop(0)
            arr.append(first_element)
            return arr
        arr = copy.deepcopy(mat)

        
        for j in range(k):
            for i in range(len(mat)):
                if i % 2 == 0 :
                    mat[i]= left_shift(mat[i])
                else:
                    mat[i]= right_shift(mat[i])
        
        return arr == mat
