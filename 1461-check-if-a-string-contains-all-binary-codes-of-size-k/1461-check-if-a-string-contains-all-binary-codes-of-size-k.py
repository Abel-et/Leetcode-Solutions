class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # calculate how could be the lenghts 
        m = pow(2,k)

        seen = set()
       
        
        for i in range(len(s)-k+1):
            binary = s[i:i+k]
            seen.add(binary)

            if len(seen) == m:
                return True
        else:
            return False
           