
class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # first we convert the lists into sets 
        x = {}
        y = {}
        
        for i in a:
            x[i] = x.get(i,0) +1
        
        for i in b:
            y[i] = y.get(i,0) +1
      
        
        for i in y.keys():
            if i not in x:
                return False
            else:
                if x[i] < y[i]:
                    return False
        else:
            return True
