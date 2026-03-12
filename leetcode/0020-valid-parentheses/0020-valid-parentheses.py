class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {')':'(','}':'{',']':'['}
        stack = []
        if len(s)%2 == 1:
            return False
        for i in s:
            if i in parentheses:
                if stack and stack[-1] != parentheses[i]:
                    return False
                elif  stack and stack[-1] == parentheses[i]:
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)
        return stack == []
