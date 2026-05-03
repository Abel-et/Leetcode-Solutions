class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
    
        n = len(goal)

        if len(s) != n:
            return False

        # back = ''

        # index = 0
        # j = 0
        # while index < n and j < len(s):
        #     if s[j] != goal [index]:
        #         back += s[j]

        #     else:
        #         index += 1
        #     j += 1
        # print(back)
        # result = s[len(back):] + back
        # print(result)
        
        # for i in range(n):
        #     if result[i] != goal[i]:
        #         return False
        # return True
        def check(s , g):
            for i in range(n):
                if s[i] != g[i]:
                    return False
            return True

        for i in range(n):
            k = s[i+1:] + s[:i+1]
            if check(k,goal):
                return True
        return False