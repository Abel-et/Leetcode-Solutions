class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        val, output = 0, 0 

        for p in s:
            
            # if p is opened prantesis
            if p == '(':
                stack.append(0)
            else:
                mult = stack.pop()

                # make update the val value
                if mult == 0:
                    val = 1
                else :
                    val = 2*mult
                if not stack:
                    output += val
                else:
                    stack[-1] += val
        return output
                
              
