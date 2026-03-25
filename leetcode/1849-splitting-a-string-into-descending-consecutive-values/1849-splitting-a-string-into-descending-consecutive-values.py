class Solution:
    def splitString(self, s: str) -> bool:
        

        def backtrack(idx,curr):
            if idx == len(s):
                for i in range(1,len(curr)):
                    if curr[i-1] - curr[i] !=1:
                        return False
                return len(curr) >=2
            for j in range(idx,len(s)):
                val = int(s[idx:j+1])
                curr.append(val)
                if backtrack(j+1,curr):
                    return True
                curr.pop()
                
            return False
        return backtrack(0,[])