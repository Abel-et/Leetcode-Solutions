class Solution:
    def isValid(self, s: str) -> bool:

        # the game is just puting the inclosed parenthese as a key and the opposite one as a value
        parentheses = {')':'(','}':'{',']':'['}

        # put in to a stack the values which are in s
        stack = []

        # if the lenght of the parentheses is odd automaticall show return false
        if len(s)%2 == 1:
            return False
        for i in s:
            # if the comming paren is inclose
            if i in parentheses:

                # and the top of the stack is not the oposite of it return  False
                if stack and stack[-1] != parentheses[i] or not stack:
                    return False
                    
                # or the top of the stack is valid to the given inclosed parenthese delete it 
                stack.pop()

            # if the give parent is opened should add to the stack
            else:
                stack.append(i)
        
        # if the stack is empty return true 
        return stack == []
