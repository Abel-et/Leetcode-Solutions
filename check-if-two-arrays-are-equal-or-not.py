class Solution:
    def checkEqual(self, a, b) -> bool:
        #code here
        x = dict()
        y = dict()
           
        for i in a:
            if i in x:
                x[i]+=1
            else:
                x[i] = 1
                    
        for i in b:
            if i in y:
                y[i]+=1
            else:
                y[i] = 1
        x_key = set(x.keys())
        y_key = set(y.keys())
            
        if x_key == y_key:
            for i in x_key:
                if x[i] != y[i]:
                        return False
            else:
                return True
        else:
            return False
            
