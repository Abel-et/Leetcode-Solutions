class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in s: 
            if i !=']':
                stack.append(i)

            else:
                store = ''

                while stack and stack[-1] != "[":
                    store = stack.pop() +store

                stack.pop()   

                num = ''
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num

                
                stack.append( int(num)*store)
                
        return ''.join(stack)
             


                
