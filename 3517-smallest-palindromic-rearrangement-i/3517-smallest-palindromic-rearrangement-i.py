class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        new_s = list(s)



        if n<3 or len(set(s)) == 1:
            return s
        
        if n%2 == 0:
            half = sorted(new_s[:n//2])
            re = sorted(half , reverse=True)
            result = half+re
           

            return "".join(result)
        else:
            mid =list(new_s[n//2])
            half = sorted(new_s[:n//2])
            re = sorted(half , reverse=True)
            result = half + mid + re
            return "".join(result)

        