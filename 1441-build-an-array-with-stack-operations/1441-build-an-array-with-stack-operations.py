class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        stack = []
        s = []
        for i in range(1,n+1):
            if i > max(target):
                break
            
            stack.append("Push")
            s.append(i)
            if i not in target:
                stack.append('Pop')
                if s :
                    s.pop()

        return stack