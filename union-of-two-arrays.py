class Solution:    
    def findUnion(self, a, b):
        # code here
        x = set(a)
        y = set(b)
        c =  x | y
        return [ i for i in c]
