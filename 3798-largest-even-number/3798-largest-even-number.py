class Solution(object):
    def largestEven(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        
        for i in range(n-1,-1,-1):
            if s and s[i] =="1":
                s=s[:i]
            elif s and s[i] == "2":
                return s
        else:
            return ""
